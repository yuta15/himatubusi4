from ...base import Applier
from ...common import Provider, Result


class AppGatewayApplier(Applier):
    def __init__(
        self,
        name: str,
        target_url: str,
        port: int,
    ) -> None:
        self.name = name
        self.target_url = target_url
        self.port = port

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "APP_GATEWAY",
            name=self.name,
            target_url=self.target_url,
            port=self.port,
        )
        return Result(True, f"Simulated gateway creation: {self.name}")
