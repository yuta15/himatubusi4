from ...base import Builder
from ...common import Request
from ...validation import choice, required_string
from .applier import ArtifactRegistryApplier


class ArtifactRegistryBuilder(Builder):
    def build(self, request: Request) -> ArtifactRegistryApplier:
        params = {"format": "DOCKER", **request.parameters}
        return ArtifactRegistryApplier(
            required_string(params, "repository_name"),
            required_string(params, "project_id"),
            required_string(params, "location"),
            choice(params, "format", ("DOCKER", "MAVEN", "NPM")),
        )
