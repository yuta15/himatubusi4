from ...base import Builder
from ...common import Request
from ...validation import required_string
from .applier import PubSubApplier


class PubSubBuilder(Builder):
    def build(self, request: Request) -> PubSubApplier:
        params = request.parameters
        return PubSubApplier(
            required_string(params, "topic_name"),
            required_string(params, "project_id"),
        )
