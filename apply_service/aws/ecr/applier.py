from ...base import Applier
from ...common import Provider, Result


class EcrApplier(Applier):
    def __init__(
        self,
        repository_name: str,
        region: str,
        scan_on_push: bool,
    ) -> None:
        self.repository_name = repository_name
        self.region = region
        self.scan_on_push = scan_on_push

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "ECR",
            repository_name=self.repository_name,
            region=self.region,
            scan_on_push=self.scan_on_push,
        )
        return Result(True, f"Simulated ECR repository creation: {self.repository_name}")
