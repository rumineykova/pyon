 #!/usr/bin/env python

"""AMQP messaging with Pika."""

import gevent
from gevent import event, coros

from pika.credentials import PlainCredentials
from pika.connection import ConnectionParameters
from pika.adapters import SelectConnection
from pika import channel as pikachannel
from pika.exceptions import NoFreeChannels

from pyon.core.bootstrap import CFG, get_sys_name
from pyon.net import channel
from pyon.util.async import blocking_cb
from pyon.util.containers import for_name
from pyon.util.log import log
from pyon.util.pool import IDPool
from pyon.net.transport import LocalTransport, LocalRouter, AMQPTransport, ComposableTransport

from collections import defaultdict

class BaseNode(object):
    """
    """

    def __init__(self):
        self.client = None
        self.running = False
        self.ready = event.Event()
        self._lock = coros.RLock()

        self.interceptors = {}  # endpoint interceptors

    def on_connection_open(self, client):
        """
        AMQP Connection Open event handler.
        TODO: Should this be in another class?
        """
        log.debug("In Node.on_connection_open")
        log.debug("client: %s" % str(client))
        client.add_on_close_callback(self.on_connection_close)
        self.client = client
        self.start_node()

    def on_connection_close(self, *a):
        """
        AMQP Connection Close event handler.
        TODO: Should this be in another class?
        """
        log.debug("In Node.on_connection_close")

    def start_node(self):
        """
        This should only be called by on_connection_opened.
        so, maybe we don't need a start_node/stop_node interface
        TODO: Does this mean only one connection is supported?
        """
        log.debug("In Node.start_node")
        self.running = True
        self.ready.set()

    def stop_node(self):
        """
        """
        log.debug("In Node.stop_node")
        self.running = False

    def channel(self, ch_type):
        """
        Create a channel on current node.
        Implement this in subclass
        name shouldn't be a parameter here
        """
        log.debug("In Node.channel")

    def _new_channel(self, ch_type, ch_number=None, transport=None):
        """
        Creates a pyon Channel based on the passed in type, and activates it for use.

        @param  transport   If specified, will wrap the underlying transport created here.
        """
        chan = ch_type()
        new_transport = self._new_transport(ch_number=ch_number)

        # create overlay transport
        if transport is not None:
            new_transport = ComposableTransport(transport, new_transport)

        chan.on_channel_open(new_transport)
        return chan

    def _new_transport(self, ch_number=None):
        """
        Creates a new transport to be used by a Channel.

        You must override this in your derived node.
        """
        raise NotImplementedError()

    def setup_interceptors(self, interceptor_cfg):
        stack = interceptor_cfg["stack"]
        defs = interceptor_cfg["interceptors"]

        interceptors = defaultdict(list)

        by_name_dict = {}
        for type_and_direction in stack:
            interceptor_names = stack[type_and_direction]
            for name in interceptor_names:
                if name in by_name_dict:
                    classinst = by_name_dict[name]
                else:
                    interceptor_def = defs[name]

                    # Instantiate and put in by_name array
                    modpath, classname  = interceptor_def['class'].rsplit('.', 1)
                    classinst           = for_name(modpath, classname)

                    # Call configure
                    classinst.configure(config = interceptor_def["config"] if "config" in interceptor_def else None)

                    # Put in by_name_dict for possible re-use
                    by_name_dict[name] = classinst

                interceptors[type_and_direction].append(classinst)

        self.interceptors = dict(interceptors)

class NodeB(BaseNode):
    """
    Blocking interface to AMQP messaging primitives.

    Wrap around Node and create blocking interface for getting channel
    objects.
    """

    def __init__(self):
        log.debug("In NodeB.__init__")
        BaseNode.__init__(self)

        self._pool = IDPool()
        self._bidir_pool = {}   # maps inactive/active our numbers (from self._pool) to channels
        self._pool_map = {}     # maps active pika channel numbers to our numbers (from self._pool)

        BaseNode.__init__(self)

    def stop_node(self):
        """
        Closes the connection to the broker, cleans up resources held by this node.
        """
        log.debug("NodeB.stop_node (running: %s)", self.running)

        if self.running:
            # clean up pooling before we shut connection
            self._destroy_pool()
            self.client.close()

        BaseNode.stop_node(self)

    def _destroy_pool(self):
        """
        Explicitly deletes pooled queues in this Node.
        """
        for chan in self._bidir_pool.itervalues():
            chan._destroy_queue()

    def _new_transport(self, ch_number=None):
        """
        Creates a new AMQPTransport with an underlying Pika channel.
        """
        amq_chan = blocking_cb(self.client.channel, 'on_open_callback', channel_number=ch_number)
        if amq_chan is None:
            log.error("AMQCHAN IS NONE THIS SHOULD NEVER HAPPEN, chan number requested: %s", ch_number)
            import traceback
            traceback.print_stack()
            raise StandardError("AMQCHAN IS NONE THIS SHOULD NEVER HAPPEN, chan number requested: %s" % ch_number)

        transport = AMQPTransport(amq_chan)
        return transport

    def channel(self, ch_type, transport=None):
        """
        Creates a Channel object with an underlying transport callback and returns it.

        @type ch_type   BaseChannel
        """
        log.debug("NodeB.channel")
        with self._lock:
            # having _queue_auto_delete on is a pre-req to being able to pool.
            if ch_type == channel.BidirClientChannel and not ch_type._queue_auto_delete:
                chid = self._pool.get_id()
                if chid in self._bidir_pool:
                    log.debug("BidirClientChannel requested, pulling from pool (%d)", chid)
                    assert not chid in self._pool_map.values()
                    ch = self._bidir_pool[chid]
                    self._pool_map[ch.get_channel_id()] = chid
                else:
                    log.debug("BidirClientChannel requested, no pool items available, creating new (%d)", chid)
                    ch = self._new_channel(ch_type, transport=transport)
                    ch.set_close_callback(self.on_channel_request_close)
                    self._bidir_pool[chid] = ch
                    self._pool_map[ch.get_channel_id()] = chid
            else:
                ch = self._new_channel(ch_type, transport=transport)
            assert ch

        return ch

    def on_channel_request_close(self, ch):
        """
        Close callback for pooled Channels.

        When a new, pooled Channel is created that this Node manages, it will specify this as the
        close callback in order to prevent that Channel from actually closing.
        """
        log.debug("NodeB: on_channel_request_close\n\tChType %s, Ch#: %d", ch.__class__, ch.get_channel_id())

        assert ch.get_channel_id() in self._pool_map
        with self._lock:
            chid = self._pool_map.pop(ch.get_channel_id())
            log.debug("Releasing BiDir pool Pika #%d, our id #%d", ch.get_channel_id(), chid)
            self._pool.release_id(chid)

            # reset channel
            ch.reset()

            # sanity check: if auto delete got turned on, we must remove this channel from the pool
            if ch._queue_auto_delete:
                log.warn("A pooled channel now has _queue_auto_delete set true, we must remove it: check what caused this as it's likely a timing error")

                self._bidir_pool.pop(chid)
                self._pool._ids_free.remove(chid)

def ioloop(connection, name=None):
    # Loop until CTRL-C
    if name:
        name = "NODE-%s" % name

    import threading
    threading.current_thread().name = name or "NODE"
    try:
        # Start our blocking loop
        log.debug("ioloop: Before start")
        connection.ioloop.start()
        log.debug("ioloop: After start")

    except KeyboardInterrupt:

        log.debug("Got keyboard interrupt")

        # Close the connection
        connection.close()

        # Loop until the connection is closed
        connection.ioloop.start()

class PyonSelectConnection(SelectConnection):
    """
    Custom-derived Pika SelectConnection to allow us to get around re-using failed channels.

    When a Channel fails, if the channel number is reused again, sometimes Pika/Rabbit will
    choke. This class overrides the _next_channel_number method in Pika, to hand out channel
    numbers that we deem safe.
    """
    def __init__(self, parameters=None, on_open_callback=None,
                 reconnection_strategy=None):
        SelectConnection.__init__(self, parameters=parameters, on_open_callback=on_open_callback, reconnection_strategy=reconnection_strategy)
        self._bad_channel_numbers = set()

    def _next_channel_number(self):
        """
        Get the next available channel number.

        This improves on Pika's implementation by using a set, so lower channel numbers can be
        re-used. It factors in channel numbers marked as bad and treats them as if they are in
        use, so no bad channel number will ever be re-used.
        """
        # Our limit is the the Codec's Channel Max or MAX_CHANNELS if it's None
        limit = self.parameters.channel_max or pikachannel.MAX_CHANNELS

        # generate a set of available channels
        available = set(xrange(1, limit+1))

        # subtract out existing channels
        available.difference_update(self._channels.keys())

        # also subtract out poison channels
        available.difference_update(self._bad_channel_numbers)

        # used all of our channels
        if len(available) == 0:
            raise NoFreeChannels()

        # get lowest available!
        ch_num = min(available)

        log.debug("_next_channel_number: %d (of %d possible, %d used, %d bad)", ch_num, len(available), len(self._channels), len(self._bad_channel_numbers))

        return ch_num

    def mark_bad_channel(self, ch_number):
        log.debug("Marking %d as a bad channel", ch_number)
        self._bad_channel_numbers.add(ch_number)

def make_node(connection_params=None, name=None, timeout=None):
    """
    Blocking construction and connection of node.

    @param connection_params  AMQP connection parameters. By default, uses CFG.server.amqp (most common use).
    """
    log.debug("In make_node")
    node = NodeB()
    connection_params = connection_params or CFG.server.amqp
    credentials = PlainCredentials(connection_params["username"], connection_params["password"])
    conn_parameters = ConnectionParameters(host=connection_params["host"], virtual_host=connection_params["vhost"], port=connection_params["port"], credentials=credentials)
    connection = PyonSelectConnection(conn_parameters , node.on_connection_open)
    ioloop_process = gevent.spawn(ioloop, connection, name=name)
    #ioloop_process = gevent.spawn(connection.ioloop.start)
    node.ready.wait(timeout=timeout)
    return node, ioloop_process
    #return node, ioloop, connection



class LocalNode(BaseNode):
    def __init__(self, router=None):
        BaseNode.__init__(self)

        self._own_router = True
        if router is not None:
            self._local_router = router
            self._own_router = False
        else:
            self._local_router = LocalRouter(get_sys_name())
        self._channel_id_pool = IDPool()

    def start_node(self):
        BaseNode.start_node(self)
        if self._own_router:
            self._local_router.start()

    def stop_node(self):
        if self.running:
            if self._own_router:
                self._local_router.stop()
        self.running = False

    def _new_transport(self, ch_number=None):
        trans = LocalTransport(self._local_router, ch_number)
        return trans

    def channel(self, ch_type, transport=None):
        ch = self._new_channel(ch_type, ch_number=self._channel_id_pool.get_id(), transport=transport)
        # @TODO keep track of all channels to close them later from the top

        ch._transport.add_on_close_callback(self._on_channel_close)
        return ch

    def _on_channel_close(self, ch, code, text):
        log.debug("ZeroMQNode._on_channel_close (%s)", ch.channel_number)
        self._channel_id_pool.release_id(ch.channel_number)

class LocalClient(object):
    def __init__(self):
        pass

    def add_on_close_callback(self, cb):
        log.debug("ignoring close callback")

def make_local_node(timeout=None, router=None):

    if router is not None:
        node = LocalNode(router=router)
    else:
        node = LocalNode()
    node.on_connection_open(LocalClient())
    node.ready.wait(timeout=timeout)

    return node, node._local_router.gl_ioloop

