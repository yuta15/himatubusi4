from ...base import Applier
from ...common import Provider, Result


class SnsApplier(Applier):
    def __init__(
        self,
        topic_name: str,
        region: str,
        fifo: bool,
    ) -> None:
        self.topic_name = topic_name
        self.region = region
        self.fifo = fifo

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "SNS",
            topic_name=self.topic_name,
            region=self.region,
            fifo=self.fifo,
        )
        return Result(True, f"Simulated SNS topic creation: {self.topic_name}")
