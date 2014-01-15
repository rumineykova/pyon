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

type_converter = {'int':int, 'string':str}

class AssertionInterceptor(BaseInternalGovernanceInterceptor):
    key = 'assert'

    def __init__(self):
        self.context = {}

    def outgoing(self, invocation):

        if invocation.message_annotations.has_key('CONVERSATION_STATUS'):
            log.debug("AssertionInterceptor.outgoing: %s", invocation.get_arg_value('process',invocation))
            self._check(invocation)

        return invocation

    def incoming(self, invocation):

        if invocation.message_annotations.get('CONVERSATION_STATUS'):
            log.debug("AssertionInterceptor.incoming: %s", invocation.get_arg_value('process',invocation))
            self._check(invocation)

        return invocation

    def _check(self, invocation):
        conv_id = invocation.get_header_value('app-conv-id', 0)
        if not self.context.has_key(conv_id):
            self.context[conv_id]= {}

        context = invocation.message_annotations.get('CONVERSATION_CONTEXT', {})
        assertion = invocation.message_annotations.get(self.key, None)

        if isinstance(invocation.message, IonObjectBase):
            payload = invocation.message.__dict__
        else:
            payload = invocation.message
        if context:
            self.add_to_context(conv_id, context, payload)

        if assertion:
            result = eval(assertion, self.context[conv_id])

            log.info("""\n
        ----------------Assertion check:---------------------------------------------
        Assertion is: =%s  \n
        payload is: %s \n
        Status: %s  \n
        --------------------------------------------------------------------------------
            """, assertion, invocation.message, result)

    def add_to_context(self, conv_id, local_context, payload):
        # positional arguments
        if not isinstance(payload, dict):
            payload_to_dict = {}
            for key, value in local_context:
                payload_to_dict[key] = payload
            payload = payload_to_dict

        if len(local_context) >0:
            if payload is None:
                raise Exception('Payload is required when the assertion_check is enabled')
            if len(local_context) != len(payload):
                raise Exception('Wrong number of payloads for the current message')
            [self.update_context(conv_id, name, type_converter[type_sig](payload[name]))
             for (name, type_sig) in local_context]

    def update_context(self, conv_id, key, value):
        self.context[conv_id][key] = value

