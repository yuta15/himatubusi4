from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import EcrApplier


class EcrBuilder(Builder):
    def build(self, request: Request) -> EcrApplier:
        params = request.parameters
        return EcrApplier(
            required_string(params, "repository_name"),
            required_string(params, "region"),
            boolean(params, "scan_on_push", True),
        )
