from ...base import Builder
from ...common import Request
from ...validation import choice, required_string
from .applier import ContainerRegistryApplier


class ContainerRegistryBuilder(Builder):
    def build(self, request: Request) -> ContainerRegistryApplier:
        params = request.parameters
        return ContainerRegistryApplier(
            required_string(params, "registry_name"),
            required_string(params, "location"),
            choice(params, "sku", ("Basic", "Standard", "Premium")),
        )
