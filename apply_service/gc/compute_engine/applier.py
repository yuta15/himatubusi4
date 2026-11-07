from ...base import Applier
from ...common import Provider, Result


class ComputeEngineApplier(Applier):
    def __init__(
        self,
        name: str,
        zone: str,
        machine_type: str,
    ) -> None:
        self.name = name
        self.zone = zone
        self.machine_type = machine_type

    def apply(self) -> Result:
        self._print(
            Provider.GOOGLE_CLOUD,
            "COMPUTE_ENGINE",
            name=self.name,
            zone=self.zone,
            machine_type=self.machine_type,
        )
        return Result(True, f"Simulated Compute Engine instance creation: {self.name}")
