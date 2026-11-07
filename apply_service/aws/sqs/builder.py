from ...base import Builder
from ...common import Request
from ...validation import integer, required_string
from .applier import SqsApplier


class SqsBuilder(Builder):
    def build(self, request: Request) -> SqsApplier:
        params = request.parameters
        return SqsApplier(
            required_string(params, "queue_name"),
            required_string(params, "region"),
            integer(params, "visibility_timeout", 0, 43200),
        )
