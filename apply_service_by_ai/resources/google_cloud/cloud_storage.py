from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, text


def create_cloud_storage(values: Mapping[str, object]) -> Result:
    bucket_name = values["bucket_name"]
    location = values["location"]
    versioning = values["versioning"]

    # TODO: 以下のprintを、これらの引数でCloud Storage bucketを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.GOOGLE_CLOUD, "CLOUD_STORAGE", {
        "bucket_name": bucket_name,
        "location": location,
        "versioning": versioning,
    }))
    return Result(True, f"Simulated Cloud Storage bucket creation: {bucket_name}")


SPEC = ResourceSpec(
    fields={
        "bucket_name": Field(text),
        "location": Field(text),
        "versioning": Field(boolean, default=False),
    },
    execute=create_cloud_storage,
)
