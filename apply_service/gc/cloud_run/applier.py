from ...base import Applier
from ...common import Provider, Result


class CloudRunApplier(Applier):
    def __init__(
        self,
        service_name: str,
        region: str,
        image: str,
        allow_unauthenticated: bool,
    ) -> None:
        self.service_name = service_name
        self.region = region
        self.image = image
        self.allow_unauthenticated = allow_unauthenticated

    def apply(self) -> Result:
        self._print(
            Provider.GOOGLE_CLOUD,
            "CLOUD_RUN",
            service_name=self.service_name,
            region=self.region,
            image=self.image,
            allow_unauthenticated=self.allow_unauthenticated,
        )
        return Result(True, f"Simulated Cloud Run service creation: {self.service_name}")
