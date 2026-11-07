from ...base import Applier
from ...common import Provider, Result


class CloudTrailApplier(Applier):
    def __init__(
        self,
        trail_name: str,
        bucket_name: str,
        multi_region: bool,
    ) -> None:
        self.trail_name = trail_name
        self.bucket_name = bucket_name
        self.multi_region = multi_region

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "CLOUD_TRAIL",
            trail_name=self.trail_name,
            bucket_name=self.bucket_name,
            multi_region=self.multi_region,
        )
        return Result(True, f"Simulated CloudTrail trail creation: {self.trail_name}")
