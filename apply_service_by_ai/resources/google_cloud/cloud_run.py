from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, text


def create_cloud_run(values: Mapping[str, object]) -> Result:
    service_name = values["service_name"]
    region = values["region"]
    image = values["image"]
    allow_unauthenticated = values["allow_unauthenticated"]

    # TODO: 以下のprintを、これらの引数でCloud Run serviceを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.GOOGLE_CLOUD, "CLOUD_RUN", {
        "service_name": service_name,
        "region": region,
        "image": image,
        "allow_unauthenticated": allow_unauthenticated,
    }))
    return Result(True, f"Simulated Cloud Run service creation: {service_name}")


SPEC = ResourceSpec(
    fields={
        "service_name": Field(text),
        "region": Field(text),
        "image": Field(text),
        "allow_unauthenticated": Field(boolean, default=False),
    },
    execute=create_cloud_run,
)
