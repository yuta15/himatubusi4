from ...base import Applier
from ...common import Provider, Result


class CloudFrontApplier(Applier):
    def __init__(
        self,
        origin_domain: str,
        enabled: bool,
    ) -> None:
        self.origin_domain = origin_domain
        self.enabled = enabled

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "CLOUD_FRONT",
            origin_domain=self.origin_domain,
            enabled=self.enabled,
        )
        return Result(True, f"Simulated CloudFront distribution creation: {self.origin_domain}")
