from ...base import Builder
from ...common import Request
from ...validation import required_string
from .applier import SecretManagerApplier


class SecretManagerBuilder(Builder):
    def build(self, request: Request) -> SecretManagerApplier:
        params = request.parameters
        return SecretManagerApplier(
            required_string(params, "secret_id"),
            required_string(params, "project_id"),
        )
