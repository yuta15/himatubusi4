from ...base import Applier
from ...common import Provider, Result


class ManagedIdentityApplier(Applier):
    def __init__(
        self,
        identity_name: str,
        location: str,
    ) -> None:
        self.identity_name = identity_name
        self.location = location

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "MANAGED_IDENTITY",
            identity_name=self.identity_name,
            location=self.location,
        )
        return Result(True, f"Simulated user-assigned managed identity creation: {self.identity_name}")
