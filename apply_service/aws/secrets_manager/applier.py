from ...base import Applier
from ...common import Provider, Result


class SecretsManagerApplier(Applier):
    def __init__(
        self,
        secret_name: str,
        region: str,
    ) -> None:
        self.secret_name = secret_name
        self.region = region

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "SECRETS_MANAGER",
            secret_name=self.secret_name,
            region=self.region,
        )
        return Result(True, f"Simulated Secrets Manager secret creation: {self.secret_name}")
