from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import one_of, text


def create_container_registry(values: Mapping[str, object]) -> Result:
    registry_name = values["registry_name"]
    location = values["location"]
    sku = values["sku"]

    # TODO: 以下のprintを、これらの引数でcontainer registryを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "CONTAINER_REGISTRY", {
        "registry_name": registry_name,
        "location": location,
        "sku": sku,
    }))
    return Result(True, f"Simulated container registry creation: {registry_name}")


SPEC = ResourceSpec(
    fields={
        "registry_name": Field(text),
        "location": Field(text),
        "sku": Field(one_of("Basic", "Standard", "Premium")),
    },
    execute=create_container_registry,
)
