from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, hostname


def create_cloud_front(values: Mapping[str, object]) -> Result:
    origin_domain = values["origin_domain"]
    enabled = values["enabled"]

    # TODO: 以下のprintを、これらの引数でCloudFrontディストリビューションを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "CLOUD_FRONT", {
        "origin_domain": origin_domain,
        "enabled": enabled,
    }))
    return Result(True, f"Simulated CloudFront distribution creation: {origin_domain}")


SPEC = ResourceSpec(
    fields={"origin_domain": Field(hostname), "enabled": Field(boolean, default=True)},
    execute=create_cloud_front,
)
