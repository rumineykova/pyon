
__author__ = 'sphenrie'


from pyon.public import Container, ImmediateProcess
from pyon.util.context import LocalContextMixin
from pyon.core.governance import get_actor_header
from pyon.core.governance.conversation.conversation_monitor_interceptor import Conversation

from interface.services.examples.hello.ihello_service  import BasicProvider
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

        # propose(string) to provider;
        # (string) from provider;
        offer = provider.ask.propose('send me your offer')

        # consult(string) to adviser;
        # (string) from adviser;
        result = adviser.ask.consult(offer)

        # propose(string) to provider;
        # (string) from provider;
        conditions = provider.ask.propose(result)

        # consult(string) to adviser;
        # (string) from  adviser;
        result = adviser.ask.consult(conditions)
        print "Returned: " + str(result)

        # accept(string) to provider;
        # () from provider;
        provider.ask.accept(conditions)

        # accept(string) to adviser;
        # () from adviser;
        adviser.ask.accept(conditions)

        c.close()

    except Exception, e:
        print e

def negotiate_nok(container):
    try:
        c, provider, adviser = start_conversation(container, 'negotiate.scr')

        # propose(string) to provider;
        # (string) from provider
        offer = provider.ask.propose('send me your offer')

        # consult(string) to adviser;
        # (string) from adviser;
        result = adviser.ask.consult(offer)
        print "Returned: " + str(result)

        # reject(string) to provider;
        # () from provider;
        provider.ask.reject('not interested')

        # reject(string) to adviser;
        # () from adviser;
        adviser.ask.reject('not interested')

        # ERROR: Cannot propose after reject
        ret = provider.ask.propose('here is my offer')
        print "Returned: " + str(ret)

        c.close()
    except Exception, e:
        print "negotiate_nok failed: " + e.message

def negotiate_assert(container):
    try:
        c, provider, adviser = start_conversation(container, 'negotiate.scr')

        # propose(string) to provider;
        # (string) from provider
        offer = provider.ask.propose('send me your offer')

        # consult(string) to adviser;
        # (string) from adviser;
        result = adviser.ask.consult(offer)
        print "Returned: " + str(result)


        # reject(string) to  provider;
        # () from provider;
        provider.ask.reject(result)

        # reject(string) to  adviser;
        # () from adviser;
        adviser.ask.reject(result)

        provider.ask.propose(offer)

        c.close()
    except Exception, e:
        print "negotiate_re" + e.message


def negotiate_guard(container):
    try:
        c, provider, adviser = start_conversation(container, 'negotiate.scr')

        # propose(string) to provider;
        # (string) from provider
        offer = provider.ask.propose('send me your offer')

        # consult(string) to adviser;
        # (string) from adviser;
        result = adviser.ask.consult(offer)
        print "Returned: " + str(result)

        for i in range(1, 3):
            # propose(string) to provider;
            # (string) from provider;
            offer = provider.ask.propose(result)

            # consult(string) to adviser;
            # (string) from adviser;
            result = adviser.ask.consult(offer)
            print "Returned: " + str(result)

        # accept(string) to  provider;
        # () from provider;
        provider.ask.accept(result)

        # accept(string) to  adviser;
        # () from adviser;
        adviser.ask.accept(result)


        c.close()
    except Exception, e:
        print "negotiate_n failed: " + e.message

if __name__ == '__main__':
    container = Container()
    container.start()
    container.stop()
