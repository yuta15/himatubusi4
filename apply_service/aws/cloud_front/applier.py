from ...base import Applier
from ...common import Provider, Result


class CloudFrontApplier(Applier):
    def __init__(
        self,
        distribution_name: str,
        origins: list[dict[str, str]],
        default_origin_id: str,
        enabled: bool,
    ) -> None:
        self.distribution_name = distribution_name
        self.origins = origins
        self.default_origin_id = default_origin_id
        self.enabled = enabled

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "CLOUD_FRONT",
            distribution_name=self.distribution_name,
            origins=self.origins,
            default_origin_id=self.default_origin_id,
            enabled=self.enabled,
        )
        return Result(True, f"Simulated CloudFront distribution creation: {self.distribution_name}")
