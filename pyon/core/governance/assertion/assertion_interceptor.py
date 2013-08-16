__author__ = 'rumi'


from pyon.core.governance.governance_interceptor import BaseInternalGovernanceInterceptor
from pyon.util.log import log


class PayloadValidationInterceptor(BaseInternalGovernanceInterceptor):

    def outgoing(self, invocation):

        log.debug("InformationModelInterceptor.outgoing: %s", invocation.get_arg_value('process',invocation))

        return invocation

    def incoming(self, invocation):

        log.debug("InformationModelInterceptor.incoming: %s", invocation.get_arg_value('process',invocation))

        return invocation