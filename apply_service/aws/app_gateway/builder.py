from ...base import Builder
from ...common import Request
from ...validation import integer, required_string
from .applier import AppGatewayApplier


class AppGatewayBuilder(Builder):
    def build(self, request: Request) -> AppGatewayApplier:
        params = request.parameters
        target_url = required_string(params, "target_url")
        if not target_url.startswith(("https://", "http://")):
            raise ValueError("target_url must start with http:// or https://")
        return AppGatewayApplier(required_string(params, "name"), target_url, integer(params, "port", 1, 65535))

