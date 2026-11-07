from ...base import Applier
from ...common import Provider, Result


class SqsApplier(Applier):
    def __init__(
        self,
        queue_name: str,
        region: str,
        visibility_timeout: int,
    ) -> None:
        self.queue_name = queue_name
        self.region = region
        self.visibility_timeout = visibility_timeout

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "SQS",
            queue_name=self.queue_name,
            region=self.region,
            visibility_timeout=self.visibility_timeout,
        )
        return Result(True, f"Simulated SQS queue creation: {self.queue_name}")
