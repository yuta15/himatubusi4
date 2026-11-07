from .common import Request, Result
from .builder_provider import BuilderProvider


class ApplyService:
    def __init__(self, builder_provider:BuilderProvider):
        self._builder_provider = builder_provider

    def apply(self, request:Request) -> Result:
        builder = self._builder_provider.provide(provider=request.provider, resource_type=request.resource_type)
        applier = builder.build(request=request)
        return applier.apply()