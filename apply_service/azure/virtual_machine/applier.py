from ...base import Applier
from ...common import Provider, Result


class VirtualMachineApplier(Applier):
    def __init__(
        self,
        name: str,
        size: str,
        disk_size_gb: int,
    ) -> None:
        self.name = name
        self.size = size
        self.disk_size_gb = disk_size_gb

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "VIRTUAL_MACHINE",
            name=self.name,
            size=self.size,
            disk_size_gb=self.disk_size_gb,
        )
        return Result(True, f"Simulated virtual machine creation: {self.name}")
