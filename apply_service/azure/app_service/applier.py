from ...base import Applier
from ...common import Provider, Result


class AppServiceApplier(Applier):
    def __init__(
        self,
        name: str,
        plan_name: str,
        runtime: str,
    ) -> None:
        self.name = name
        self.plan_name = plan_name
        self.runtime = runtime

    def apply(self) -> Result:
        self._print(
            Provider.AZURE,
            "APP_SERVICE",
            name=self.name,
            plan_name=self.plan_name,
            runtime=self.runtime,
        )
        return Result(True, f"Simulated web app creation: {self.name}")
