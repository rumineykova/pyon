
__author__ = 'sphenrie'


from pyon.public import Container, ImmediateProcess
#from pyon.ion.endpoint import ProcessRPCClient
from pyon.util.context import LocalContextMixin
from pyon.core.governance import get_actor_header
from pyon.core.governance.conversation.conversation_monitor_interceptor import Conversation

from interface.services.examples.hello.ihello_service  import HelloServiceProcessClient, BasicProvider
from interface.services.icontainer_agent import ContainerAgentProcessClient
import uuid as _uuid

def uuid():
    return str(_uuid.uuid4())[0:6]

class FakeProcess(LocalContextMixin):
    name = 'hello_client'
    id = ''

class HelloClientProcess(ImmediateProcess):
    """
    bin/pycc -x examples.hello_client.HelloClientProcess
    """
    def on_init(self):
        pass

    def on_start(self):

        text = self.CFG.get("text", 'mytext 123')
        actor_id = self.CFG.get("actor_id", 'anonymous')
        container_name = self.CFG.get("kill_container", None)

        #hello_client(self.container, actor_id, text )

        if container_name:
            cc_client = ContainerAgentProcessClient(node=self.container.node, process=self, name=container_name)
            cc_client.stop()

    def on_quit(self):
        pass

def start_conversation(container, protocol):
    c = Conversation(protocol)
    provider = BasicProvider(node=container.node, process=FakeProcess(),
                             conversation=c, role='provider')

    adviser = BasicProvider(node=container.node, process=FakeProcess(),
                            conversation=c, role='adviser')
    return c, provider, adviser

# Test
def negotiate_ok(container):

    try:
        c, provider, adviser = start_conversation(container, 'negotiate.scr')

        # get_offer(text:string) to provider;
        # (offer:string) from provider;
        offer = provider.send.get_offer('send me your offer')

        # consult(text:string) to adviser;
        # (result:string) from adviser;
        result = adviser.send.consult(offer)

        # propose(text:string) to provider;
        # (x:string) from provider;
        conditions = provider.send.propose(result)

        # consult(text:string) to adviser;
        # (x:string) from  adviser;
        adviser.send.consult(conditions)

        # accept(text:string) to  provider;
        # (x:string) from provider;
        provider.send.accept(conditions)

        # accept() to  adviser;
        # () from adviser;
        adviser.send.accept(conditions)

        c.close()

    except Exception, e:
        print e

def negotiate_nok(container):
    try:
        c, provider, adviser = start_conversation(container, 'negotiate.scr')

        # get_offer(text:string) to provider;
        # (offer:string) from provider
        offer = provider.send.get_offer('send me your offer')

        # consult(text:string) to adviser;
        # (result:string) from adviser;
        result = adviser.send.consult(offer)
        print "Returned: " + str(result)

        # reject(text:string) to provider;
        # (x:string) from provider;
        ret = provider.send.reject('not interested')
        print "Returned: " + str(ret)

        ret = provider.send.propose('here is my offer')
        print "Returned: " + str(ret)

        c.close()
    except Exception, e:
        print "negotiate_nok failed: " + e.message

def negotiate_assert(container):
    try:
        c, provider, adviser = start_conversation(container, 'negotiate.scr')

        # get_offer(text:string) to provider;
        # (offer:string) from provider
        offer = provider.send.get_offer('send me your offer')

        # consult(text:string) to adviser;
        # (result:string) from adviser;
        result = adviser.send.consult(offer)
        print "Returned: " + str(result)

        # propose(text:string) to provider;
        # (x:string) from provider;
        provider.send.propose(offer)

        c.close()
    except Exception, e:
        print "negotiate_re" + e.message


def negotiate_guard(container):
    try:
        c, provider, adviser = start_conversation(container, 'negotiate.scr')

        # get_offer(text:string) to provider;
        # (offer:string) from provider
        offer = provider.send.get_offer('send me your offer')

        # consult(text:string) to adviser;
        # (result:string) from adviser;
        result = adviser.send.consult(offer)
        print "Returned: " + str(result)

        for i in range(1, 3):
            # propose(text:string) to provider;
            # (x:string) from provider;
            reply = provider.send.propose(result)

            # consult() to adviser;
            # () from adviser;
            result = adviser.send.consult(offer)
            print "Returned: " + str(result)

        print "Returned: " + str(reply)

        c.close()
    except Exception, e:
        print "negotiate_n failed: " + e.message

if __name__ == '__main__':
    container = Container()
    container.start()
    container.stop()
