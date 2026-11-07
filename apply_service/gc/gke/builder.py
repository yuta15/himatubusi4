from ...base import Builder
from ...common import Request
from ...validation import boolean, integer, required_string
from .applier import GkeApplier


class GkeBuilder(Builder):
    def build(self, request: Request) -> GkeApplier:
        params = request.parameters
        return GkeApplier(
            required_string(params, "cluster_name"), required_string(params, "location"),
            integer(params, "node_count", 1, 100), boolean(params, "private_cluster", False),
        )

