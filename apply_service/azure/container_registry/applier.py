from ...base import Applier
from ...common import Provider, Result


class ContainerRegistryApplier(Applier):
    def __init__(
        self,
        registry_name: str,
        location: str,
        sku: str,
    ) -> None:
        self.registry_name = registry_name
        self.location = location
        self.sku = sku

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "CONTAINER_REGISTRY",
            registry_name=self.registry_name,
            location=self.location,
            sku=self.sku,
        )
        return Result(True, f"Simulated container registry creation: {self.registry_name}")
