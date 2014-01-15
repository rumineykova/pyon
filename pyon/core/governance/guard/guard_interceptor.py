from pyon.core.object import IonObjectBase

__author__ = 'rumi'

from pyon.core.governance.governance_interceptor import BaseInternalGovernanceInterceptor
from pyon.util.log import log
from pyon.core.governance.conversation.extensions.simple_logic import AssertionParser


class ExceptionFailAssertion(Exception):
    """This is the FSM Exception class."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return `self.value`


class GuardInterceptor(BaseInternalGovernanceInterceptor):
    key = 'guard'

    def __init__(self):
        self.context = {}

    def outgoing(self, invocation):

        if invocation.message_annotations.has_key('CONVERSATION_STATUS'):
            log.debug("AssertionInterceptor.outgoing: %s", invocation.get_arg_value('process', invocation))
            self._check(invocation)

        return invocation

    def incoming(self, invocation):

        if invocation.message_annotations.get('CONVERSATION_STATUS'):
            log.debug("AssertionInterceptor.incoming: %s", invocation.get_arg_value('process', invocation))
            self._check(invocation)

        return invocation

    def _check(self, invocation):
        conv_id = invocation.get_header_value('app-conv-id', 0)
        if not self.context.has_key(conv_id):
            self.context[conv_id] = -1

        assertion = invocation.message_annotations.get(self.key, None)
        if assertion:
            result = True
            repeat = self.context[conv_id]
            if repeat<0:
                self.context[conv_id] = 1
            else:
                self.context[conv_id] = repeat + 1
                result = eval(assertion, {'repeat': self.context[conv_id]})
            log.info("""\n
        ----------------Guard check:----------------------------------------------------
        Assertion is: =%s  \n
        Repeats: = %s \n
        Status: %s  \n
        --------------------------------------------------------------------------------
            """, assertion, self.context[conv_id], result)

    def update_context(self, conv_id, key, value):
        self.context[conv_id][key] = value

