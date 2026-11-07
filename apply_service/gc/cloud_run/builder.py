from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import CloudRunApplier


class CloudRunBuilder(Builder):
    def build(self, request: Request) -> CloudRunApplier:
        params = request.parameters
        return CloudRunApplier(
            required_string(params, "service_name"),
            required_string(params, "region"),
            required_string(params, "image"),
            boolean(params, "allow_unauthenticated", False),
        )
