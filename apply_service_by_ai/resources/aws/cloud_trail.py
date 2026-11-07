from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, text


def create_cloud_trail(values: Mapping[str, object]) -> Result:
    trail_name = values["trail_name"]
    bucket_name = values["bucket_name"]
    multi_region = values["multi_region"]

    # TODO: 以下のprintを、これらの引数でCloudTrailを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "CLOUD_TRAIL", {
        "trail_name": trail_name,
        "bucket_name": bucket_name,
        "multi_region": multi_region,
    }))
    return Result(True, f"Simulated CloudTrail trail creation: {trail_name}")


SPEC = ResourceSpec(
    fields={
        "trail_name": Field(text),
        "bucket_name": Field(text),
        "multi_region": Field(boolean, default=True),
    },
    execute=create_cloud_trail,
)
