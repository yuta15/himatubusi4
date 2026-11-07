from ...base import Builder
from ...common import Request
from ...validation import choice, required_string
from .applier import AppServiceApplier


class AppServiceBuilder(Builder):
    def build(self, request: Request) -> AppServiceApplier:
        params = request.parameters
        return AppServiceApplier(
            required_string(params, "name"), required_string(params, "plan_name"),
            choice(params, "runtime", ("python", "node", "dotnet")),
        )

