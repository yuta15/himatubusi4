from ...base import Builder
from ...common import Request
from ...validation import required_string
from .applier import SecretsManagerApplier


class SecretsManagerBuilder(Builder):
    def build(self, request: Request) -> SecretsManagerApplier:
        params = request.parameters
        return SecretsManagerApplier(
            required_string(params, "secret_name"),
            required_string(params, "region"),
        )
