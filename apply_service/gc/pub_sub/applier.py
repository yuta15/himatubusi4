from ...base import Applier
from ...common import Provider, Result


class PubSubApplier(Applier):
    def __init__(
        self,
        topic_name: str,
        project_id: str,
    ) -> None:
        self.topic_name = topic_name
        self.project_id = project_id

    def apply(self) -> Result:
        self._print(
            Provider.GOOGLE_CLOUD,
            "PUB_SUB",
            topic_name=self.topic_name,
            project_id=self.project_id,
        )
        return Result(True, f"Simulated Pub/Sub topic creation: {self.topic_name}")
