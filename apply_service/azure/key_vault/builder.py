from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import KeyVaultApplier


class KeyVaultBuilder(Builder):
    def build(self, request: Request) -> KeyVaultApplier:
        params = request.parameters
        return KeyVaultApplier(
            required_string(params, "vault_name"),
            required_string(params, "location"),
            boolean(params, "soft_delete", True),
        )
