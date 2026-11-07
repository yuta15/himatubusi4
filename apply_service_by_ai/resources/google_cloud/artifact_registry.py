from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import one_of, text


def create_artifact_registry(values: Mapping[str, object]) -> Result:
    repository_name = values["repository_name"]
    project_id = values["project_id"]
    location = values["location"]
    format = values["format"]

    # TODO: 以下のprintを、これらの引数でArtifact Registry repositoryを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.GOOGLE_CLOUD, "ARTIFACT_REGISTRY", {
        "repository_name": repository_name,
        "project_id": project_id,
        "location": location,
        "format": format,
    }))
    return Result(True, f"Simulated Artifact Registry repository creation: {repository_name}")


SPEC = ResourceSpec(
    fields={
        "repository_name": Field(text),
        "project_id": Field(text),
        "location": Field(text),
        "format": Field(one_of("DOCKER", "MAVEN", "NPM"), default="DOCKER"),
    },
    execute=create_artifact_registry,
)
