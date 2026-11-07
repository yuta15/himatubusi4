from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import one_of, text


def create_event_hubs(values: Mapping[str, object]) -> Result:
    namespace_name = values["namespace_name"]
    location = values["location"]
    sku = values["sku"]

    # TODO: 以下のprintを、これらの引数でEvent Hubs namespaceを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "EVENT_HUBS", {
        "namespace_name": namespace_name,
        "location": location,
        "sku": sku,
    }))
    return Result(True, f"Simulated Event Hubs namespace creation: {namespace_name}")


SPEC = ResourceSpec(
    fields={
        "namespace_name": Field(text),
        "location": Field(text),
        "sku": Field(one_of("Basic", "Standard", "Premium"), default="Standard"),
    },
    execute=create_event_hubs,
)
