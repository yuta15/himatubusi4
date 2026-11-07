from ...base import Applier
from ...common import Provider, Result


class ServiceBusApplier(Applier):
    def __init__(
        self,
        namespace_name: str,
        location: str,
        sku: str,
    ) -> None:
        self.namespace_name = namespace_name
        self.location = location
        self.sku = sku

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "SERVICE_BUS",
            namespace_name=self.namespace_name,
            location=self.location,
            sku=self.sku,
        )
        return Result(True, f"Simulated Service Bus namespace creation: {self.namespace_name}")
