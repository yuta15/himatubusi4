from ...base import Builder
from ...common import Request
from ...validation import required_string
from .applier import ManagedIdentityApplier


class ManagedIdentityBuilder(Builder):
    def build(self, request: Request) -> ManagedIdentityApplier:
        params = request.parameters
        return ManagedIdentityApplier(
            required_string(params, "identity_name"),
            required_string(params, "location"),
        )
