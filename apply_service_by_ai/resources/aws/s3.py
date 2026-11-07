from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, string_length, text


def create_s3(values: Mapping[str, object]) -> Result:
    bucket_name = values["bucket_name"]
    region = values["region"]
    versioning = values["versioning"]

    # TODO: 以下のprintを、これらの引数でS3バケットを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "S3", {
        "bucket_name": bucket_name,
        "region": region,
        "versioning": versioning,
    }))
    return Result(True, f"Simulated S3 bucket creation: {bucket_name}")


SPEC = ResourceSpec(
    fields={
        "bucket_name": Field(string_length(3, 63)),
        "region": Field(text),
        "versioning": Field(boolean, default=False),
    },
    execute=create_s3,
)
