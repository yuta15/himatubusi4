from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, text


def create_key_vault(values: Mapping[str, object]) -> Result:
    vault_name = values["vault_name"]
    location = values["location"]
    soft_delete = values["soft_delete"]

    # TODO: 以下のprintを、これらの引数でKey Vaultを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "KEY_VAULT", {
        "vault_name": vault_name,
        "location": location,
        "soft_delete": soft_delete,
    }))
    return Result(True, f"Simulated Key Vault creation: {vault_name}")


SPEC = ResourceSpec(
    fields={
        "vault_name": Field(text),
        "location": Field(text),
        "soft_delete": Field(boolean, default=True),
    },
    execute=create_key_vault,
)
