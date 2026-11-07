from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import integer, text


def create_log_analytics(values: Mapping[str, object]) -> Result:
    workspace_name = values["workspace_name"]
    location = values["location"]
    retention_days = values["retention_days"]

    # TODO: 以下のprintを、これらの引数でLog Analytics workspaceを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "LOG_ANALYTICS", {
        "workspace_name": workspace_name,
        "location": location,
        "retention_days": retention_days,
    }))
    return Result(True, f"Simulated Log Analytics workspace creation: {workspace_name}")


SPEC = ResourceSpec(
    fields={
        "workspace_name": Field(text),
        "location": Field(text),
        "retention_days": Field(integer(30, 730), default=30),
    },
    execute=create_log_analytics,
)
