from ...base import Applier
from ...common import Provider, Result


class StorageAccountApplier(Applier):
    def __init__(
        self,
        account_name: str,
        location: str,
        replication: str,
    ) -> None:
        self.account_name = account_name
        self.location = location
        self.replication = replication

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "STORAGE_ACCOUNT",
            account_name=self.account_name,
            location=self.location,
            replication=self.replication,
        )
        return Result(True, f"Simulated storage account creation: {self.account_name}")
