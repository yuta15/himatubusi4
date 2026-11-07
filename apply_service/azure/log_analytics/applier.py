from ...base import Applier
from ...common import Provider, Result


class LogAnalyticsApplier(Applier):
    def __init__(
        self,
        workspace_name: str,
        location: str,
        retention_days: int,
    ) -> None:
        self.workspace_name = workspace_name
        self.location = location
        self.retention_days = retention_days

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "LOG_ANALYTICS",
            workspace_name=self.workspace_name,
            location=self.location,
            retention_days=self.retention_days,
        )
        return Result(True, f"Simulated Log Analytics workspace creation: {self.workspace_name}")
