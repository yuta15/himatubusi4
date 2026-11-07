from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import SnsApplier


class SnsBuilder(Builder):
    def build(self, request: Request) -> SnsApplier:
        params = request.parameters
        return SnsApplier(
            required_string(params, "topic_name"),
            required_string(params, "region"),
            boolean(params, "fifo", False),
        )
