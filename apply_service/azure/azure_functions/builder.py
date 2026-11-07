from ...base import Builder
from ...common import Request
from ...validation import choice, required_string
from .applier import AzureFunctionsApplier


class AzureFunctionsBuilder(Builder):
    def build(self, request: Request) -> AzureFunctionsApplier:
        params = request.parameters
        return AzureFunctionsApplier(
            required_string(params, "name"), choice(params, "runtime", ("python", "node", "dotnet")),
            required_string(params, "storage_account"),
        )

