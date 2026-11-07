from ...base import Applier
from ...common import Provider, Result


class KeyVaultApplier(Applier):
    def __init__(
        self,
        vault_name: str,
        location: str,
        soft_delete: bool,
    ) -> None:
        self.vault_name = vault_name
        self.location = location
        self.soft_delete = soft_delete

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "KEY_VAULT",
            vault_name=self.vault_name,
            location=self.location,
            soft_delete=self.soft_delete,
        )
        return Result(True, f"Simulated Key Vault creation: {self.vault_name}")
