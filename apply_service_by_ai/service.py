from collections.abc import Mapping
from types import MappingProxyType

from .resources import aws, azure, google_cloud
from .models import Provider, Request, Result
from .resource import ResourceSpec

type ResourceKey = tuple[Provider, str]


def default_resources() -> dict[ResourceKey, ResourceSpec]:
    return {
        (provider, name): spec
        for provider, resources in (
            (Provider.AWS, aws.RESOURCES),
            (Provider.AZURE, azure.RESOURCES),
            (Provider.GOOGLE_CLOUD, google_cloud.RESOURCES),
        )
        for name, spec in resources.items()
    }


class ApplyService:
    def __init__(
        self,
        resources: Mapping[ResourceKey, ResourceSpec] | None = None,
    ) -> None:
        self._resources = MappingProxyType(dict(default_resources() if resources is None else resources))

    def apply(self, request: Request) -> Result:
        if not isinstance(request.resource_type, str):
            raise ValueError("resource_type must be a string")
        resource_type = request.resource_type.upper()
        try:
            spec = self._resources[(request.provider, resource_type)]
        except KeyError:
            raise ValueError(f"Unsupported resource: {request.provider}/{request.resource_type}") from None
        if not isinstance(request.parameters, Mapping):
            raise ValueError("parameters must be a mapping")

        values = spec.validate(request.parameters)
        return spec.execute(values)
