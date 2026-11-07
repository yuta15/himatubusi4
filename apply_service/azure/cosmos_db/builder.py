from ...base import Builder
from ...common import Request
from ...validation import integer, required_string
from .applier import CosmosDbApplier


class CosmosDbBuilder(Builder):
    def build(self, request: Request) -> CosmosDbApplier:
        params = request.parameters
        throughput = integer(params, "throughput", 400, 10000)
        if throughput % 100:
            raise ValueError("throughput must be a multiple of 100")
        return CosmosDbApplier(
            required_string(params, "account_name"), required_string(params, "database_name"), throughput
        )

