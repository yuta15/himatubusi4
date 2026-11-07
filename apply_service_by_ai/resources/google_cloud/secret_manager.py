from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import text


def create_secret_manager(values: Mapping[str, object]) -> Result:
    secret_id = values["secret_id"]
    project_id = values["project_id"]

    # TODO: 以下のprintを、これらの引数でSecret Manager secretを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.GOOGLE_CLOUD, "SECRET_MANAGER", {
        "secret_id": secret_id,
        "project_id": project_id,
    }))
    return Result(True, f"Simulated Secret Manager secret creation: {secret_id}")


SPEC = ResourceSpec(
    fields={
        "secret_id": Field(text),
        "project_id": Field(text),
    },
    execute=create_secret_manager,
)
