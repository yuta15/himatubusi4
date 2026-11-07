from ...base import Applier
from ...common import Provider, Result


class SecretManagerApplier(Applier):
    def __init__(
        self,
        secret_id: str,
        project_id: str,
    ) -> None:
        self.secret_id = secret_id
        self.project_id = project_id

    def apply(self) -> Result:
        self._print(
            Provider.GOOGLE_CLOUD,
            "SECRET_MANAGER",
            secret_id=self.secret_id,
            project_id=self.project_id,
        )
        return Result(True, f"Simulated Secret Manager secret creation: {self.secret_id}")
