from ...base import Applier
from ...common import Provider, Result


class CosmosDbApplier(Applier):
    def __init__(
        self,
        account_name: str,
        database_name: str,
        throughput: int,
    ) -> None:
        self.account_name = account_name
        self.database_name = database_name
        self.throughput = throughput

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "COSMOS_DB",
            account_name=self.account_name,
            database_name=self.database_name,
            throughput=self.throughput,
        )
        return Result(True, f"Simulated Cosmos DB creation: {self.database_name}")
