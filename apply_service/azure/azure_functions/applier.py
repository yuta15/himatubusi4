from ...base import Applier
from ...common import Provider, Result


class AzureFunctionsApplier(Applier):
    def __init__(
        self,
        name: str,
        runtime: str,
        storage_account: str,
    ) -> None:
        self.name = name
        self.runtime = runtime
        self.storage_account = storage_account

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "AZURE_FUNCTIONS",
            name=self.name,
            runtime=self.runtime,
            storage_account=self.storage_account,
        )
        return Result(True, f"Simulated function app creation: {self.name}")
