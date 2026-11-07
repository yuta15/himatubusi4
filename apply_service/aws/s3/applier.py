from ...base import Applier
from ...common import Provider, Result


class S3Applier(Applier):
    def __init__(
        self,
        bucket_name: str,
        region: str,
        versioning: bool,
    ) -> None:
        self.bucket_name = bucket_name
        self.region = region
        self.versioning = versioning

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "S3",
            bucket_name=self.bucket_name,
            region=self.region,
            versioning=self.versioning,
        )
        return Result(True, f"Simulated S3 bucket creation: {self.bucket_name}")
