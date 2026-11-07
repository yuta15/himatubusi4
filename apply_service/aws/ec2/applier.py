from ...base import Applier
from ...common import Provider, Result


class Ec2Applier(Applier):
    def __init__(
        self,
        name: str,
        region: str,
        instance_type: str,
    ) -> None:
        self.name = name
        self.region = region
        self.instance_type = instance_type

    def apply(self) -> Result:
        self._print(
            Provider.AWS,
            "EC2",
            name=self.name,
            region=self.region,
            instance_type=self.instance_type,
        )
        return Result(True, f"Simulated EC2 instance creation: {self.name}")
