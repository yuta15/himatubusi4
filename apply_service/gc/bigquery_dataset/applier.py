from ...base import Applier
from ...common import Provider, Result


class BigQueryDatasetApplier(Applier):
    def __init__(
        self,
        dataset_id: str,
        project_id: str,
        location: str,
    ) -> None:
        self.dataset_id = dataset_id
        self.project_id = project_id
        self.location = location

    def apply(self) -> Result:
        self._print(
            Provider.GOOGLE_CLOUD,
            "BIGQUERY_DATASET",
            dataset_id=self.dataset_id,
            project_id=self.project_id,
            location=self.location,
        )
        return Result(True, f"Simulated BigQuery dataset creation: {self.dataset_id}")
