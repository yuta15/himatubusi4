from ...base import Builder
from ...common import Request
from ...validation import choice, required_string
from .applier import EventHubsApplier


class EventHubsBuilder(Builder):
    def build(self, request: Request) -> EventHubsApplier:
        params = {"sku": "Standard", **request.parameters}
        return EventHubsApplier(
            required_string(params, "namespace_name"),
            required_string(params, "location"),
            choice(params, "sku", ("Basic", "Standard", "Premium")),
        )
