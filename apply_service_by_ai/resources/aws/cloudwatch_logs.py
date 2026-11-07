from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import integer, text


def create_cloudwatch_logs(values: Mapping[str, object]) -> Result:
    log_group_name = values["log_group_name"]
    region = values["region"]
    retention_days = values["retention_days"]

    # TODO: 以下のprintを、これらの引数でCloudWatch Logs log groupを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "CLOUDWATCH_LOGS", {
        "log_group_name": log_group_name,
        "region": region,
        "retention_days": retention_days,
    }))
    return Result(True, f"Simulated CloudWatch Logs log group creation: {log_group_name}")


SPEC = ResourceSpec(
    fields={
        "log_group_name": Field(text),
        "region": Field(text),
        "retention_days": Field(integer(1, 365), default=30),
    },
    execute=create_cloudwatch_logs,
)
