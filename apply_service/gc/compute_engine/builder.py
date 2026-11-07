from ...base import Builder
from ...common import Request
from ...validation import required_string
from .applier import ComputeEngineApplier


class ComputeEngineBuilder(Builder):
    def build(self, request: Request) -> ComputeEngineApplier:
        params = request.parameters
        return ComputeEngineApplier(
            required_string(params, "name"), required_string(params, "zone"),
            required_string(params, "machine_type"),
        )

