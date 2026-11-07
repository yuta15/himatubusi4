from ...base import Applier
from ...common import Provider, Result


class CloudStorageApplier(Applier):
    def __init__(
        self,
        bucket_name: str,
        location: str,
        versioning: bool,
    ) -> None:
        self.bucket_name = bucket_name
        self.location = location
        self.versioning = versioning

    def apply(self) -> Result:
        self._print(
            Provider.GOOGLE_CLOUD,
            "CLOUD_STORAGE",
            bucket_name=self.bucket_name,
            location=self.location,
            versioning=self.versioning,
        )
        return Result(True, f"Simulated Cloud Storage bucket creation: {self.bucket_name}")
