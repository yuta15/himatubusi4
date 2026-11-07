from ...base import Applier
from ...common import Provider, Result


class CloudWatchLogsApplier(Applier):
    def __init__(
        self,
        log_group_name: str,
        region: str,
        retention_days: int,
    ) -> None:
        self.log_group_name = log_group_name
        self.region = region
        self.retention_days = retention_days

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "CLOUDWATCH_LOGS",
            log_group_name=self.log_group_name,
            region=self.region,
            retention_days=self.retention_days,
        )
        return Result(True, f"Simulated CloudWatch Logs log group creation: {self.log_group_name}")
