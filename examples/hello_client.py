
__author__ = 'sphenrie'
from pyon.public import Container, ImmediateProcess
from pyon.util.context import LocalContextMixin
from pyon.ion.conversation import CONV, generate_id

from interface.services.examples.hello.ihello_service  import HelloServiceProcessClient
from interface.services.icontainer_agent import ContainerAgentProcessClient

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

        hello_client(self.container, actor_id, text )

        if container_name:
            cc_client = ContainerAgentProcessClient(node=self.container.node, process=self, name=container_name)
            cc_client.stop()

    def on_quit(self):
        pass

"""
Correct execution of application level protocol composed of two consecutive RPC calls
"""
def hello_client_correct(container, text='mytext 123'):
    try:
        client = HelloServiceProcessClient(node=container.node, process=FakeProcess())

        cid = generate_id()

        ret = client.hello(text, headers = {'conv-cmd':'start', 'spec': 'hello', 'app-conv-id':cid})
        print "Returned: " + str(ret)

        ret = client.how_are_you(text, headers = {'conv-cmd':'end', 'app-conv-id':cid})
        print "Returned: " + str(ret)

    except Exception, e:
        print "client.hello() failed: " + e.message

"""
Code not compliant to its protocol: First message is skipped.
"""
def hello_client_wrong1(container, text='mytext 123'):
    try:
        client = HelloServiceProcessClient(node=container.node, process=FakeProcess())

        cid = generate_id()

        ret = client.how_are_you(text, headers = {'conv-cmd':'start', 'spec': 'hello', 'app-conv-id':cid})
        print "Returned: " + str(ret)

    except Exception, e:
        print "client.hello() failed: " + e.message

"""
Code not compliant to its protocol: First message is send twice.
"""
def hello_client_wrong2(container, text='mytext 123'):
    try:
        client = HelloServiceProcessClient(node=container.node, process=FakeProcess())

        cid = generate_id()

        ret = client.hello(text, headers = {'conv-cmd':'start', 'spec':'hello', 'app-conv-id': cid})

        print "Returned: " + str(ret)

        ret = client.hello(text, headers = {'conv-cmd':'end', 'app-conv-id': cid})
        print "Returned: " + str(ret)

    except Exception, e:
        print "client.hello() failed: " + e.message

def hello_client_wrong3(container, text='mytext 123'):
    try:
        client = HelloServiceProcessClient(node=container.node, process=FakeProcess())

        cid = generate_id()

        ret = client.hello(text, headers = {'conv-cmd':'start', 'spec':'hello', 'app-conv-id':'1234'})
        print "Returned: " + str(ret)

        ret = client.hello(text, headers = {'app-conv-id':cid})
        print "Returned: " + str(ret)

        ret = client.how_are_you(text, headers = {'conv-cmd':'end', 'app-conv-id':'1234'})
        print "Returned: " + str(ret)

    except Exception, e:
        print "client.hello() failed: " + e.message

"""
Send a start message to a conversation that is already running.
"""
def hello_client_wrong4(container, text='mytext 123'):
    try:
        client = HelloServiceProcessClient(node=container.node, process=FakeProcess())

        cid = generate_id()

        ret = client.hello(text, headers = {'conv-cmd':'start', 'spec':'hello', 'app-conv-id': cid})

        print "Returned: " + str(ret)

        ret = client.hello(text, headers = {'conv-cmd':'start', 'app-conv-id': cid})
        print "Returned: " + str(ret)

    except Exception, e:
        print "client.hello() failed: " + e.message

"""
Send a lost message without closing he conversation.
"""
def hello_client_wrong5(container, text='mytext 123'):
    try:
        client = HelloServiceProcessClient(node=container.node, process=FakeProcess())
        cid = generate_id()

        ret = client.hello(text, headers = {'conv-cmd':'start', 'spec':'hello', 'app-conv-id': cid})

        print "Returned: " + str(ret)

        ret = client.how_are_you(text, headers = {'app-conv-id': cid})
        print "Returned: " + str(ret)

        ret = client.how_are_you(text, headers = {'conv-cmd':'end', 'app-conv-id': cid})
        print "Returned: " + str(ret)

    except Exception, e:
        print "client.hello() failed: " + e.message

def hello_client_correct_interleave(container, text='mytext 123'):
    try:
        client1 = HelloServiceProcessClient(node=container.node, process=FakeProcess())

        client2 = HelloServiceProcessClient(node=container.node, process=FakeProcess())

        cid1 = generate_id()

        cid2 = generate_id()

        ret = client1.hello(text, headers = {'conv-cmd':'start', 'spec':'hello', 'app-conv-id': cid1})
        print "Returned: " + str(ret)

        ret = client2.hello(text, headers = {'conv-cmd':'start', 'spec':'hello', 'app-conv-id': cid2})
        print "Returned: " + str(ret)


        ret = client1.how_are_you(text, headers = {'conv-cmd':'end', 'app-conv-id': cid1})
        print "Returned: " + str(ret)

        ret = client2.how_are_you(text, headers = {'conv-cmd':'end', 'app-conv-id': cid2})
        print "Returned: " + str(ret)

    except Exception, e:
        print "client.hello() failed: " + e.message

"""
Execute the same protocol for consecutively.
"""
def hello_client_correct_sameid(container, text='mytext 123'):
    try:
        client1 = HelloServiceProcessClient(node=container.node, process=FakeProcess())
        cid1 = generate_id()

        ret = client1.hello(text, headers = {'conv-cmd':'start', 'spec':'hello', 'app-conv-id': cid1})
        print "Returned: " + str(ret)

        ret = client1.how_are_you(text, headers = {'conv-cmd':'end', 'app-conv-id': cid1})
        print "Returned: " + str(ret)

        ret = client1.hello(text, headers = {'conv-cmd':'start', 'spec':'hello', 'app-conv-id': cid1})
        print "Returned: " + str(ret)

        ret = client1.how_are_you(text, headers = {'conv-cmd':'end', 'app-conv-id': cid1})
        print "Returned: " + str(ret)

    except Exception, e:
        print "client.hello() failed: " + e.message

def hello_client():
    pass

def hello_client_correct_do(container, actor_id='anonymous', text='mytext 123'):
    hello_client_correct(container, actor_id, text, 'Query_instrument')



if __name__ == '__main__':

    container = Container()
    container.start() # :(
    hello_client(container)
    container.stop()
