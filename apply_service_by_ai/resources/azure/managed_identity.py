from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import text


def create_managed_identity(values: Mapping[str, object]) -> Result:
    identity_name = values["identity_name"]
    location = values["location"]

    # TODO: 以下のprintを、これらの引数でuser-assigned managed identityを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "MANAGED_IDENTITY", {
        "identity_name": identity_name,
        "location": location,
    }))
    return Result(True, f"Simulated user-assigned managed identity creation: {identity_name}")


SPEC = ResourceSpec(
    fields={
        "identity_name": Field(text),
        "location": Field(text),
    },
    execute=create_managed_identity,
)
