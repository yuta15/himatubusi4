from ...base import Builder
from ...common import Request
from ...validation import choice, required_string
from .applier import ServiceBusApplier


class ServiceBusBuilder(Builder):
    def build(self, request: Request) -> ServiceBusApplier:
        params = request.parameters
        return ServiceBusApplier(
            required_string(params, "namespace_name"),
            required_string(params, "location"),
            choice(params, "sku", ("Basic", "Standard", "Premium")),
        )
