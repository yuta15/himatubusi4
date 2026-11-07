from ...base import Applier
from ...common import Provider, Result


class ArtifactRegistryApplier(Applier):
    def __init__(
        self,
        repository_name: str,
        project_id: str,
        location: str,
        format: str,
    ) -> None:
        self.repository_name = repository_name
        self.project_id = project_id
        self.location = location
        self.format = format

    def apply(self) -> Result:
        self._print(
            Provider.GOOGLE_CLOUD,
            "ARTIFACT_REGISTRY",
            repository_name=self.repository_name,
            project_id=self.project_id,
            location=self.location,
            format=self.format,
        )
        return Result(True, f"Simulated Artifact Registry repository creation: {self.repository_name}")
