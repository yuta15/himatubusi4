from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import one_of, storage_account_name, text


def create_storage_account(values: Mapping[str, object]) -> Result:
    account_name = values["account_name"]
    location = values["location"]
    replication = values["replication"]

    # TODO: 以下のprintを、これらの引数でストレージアカウントを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "STORAGE_ACCOUNT", {
        "account_name": account_name,
        "location": location,
        "replication": replication,
    }))
    return Result(True, f"Simulated storage account creation: {account_name}")


SPEC = ResourceSpec(
    fields={
        "account_name": Field(storage_account_name),
        "location": Field(text),
        "replication": Field(one_of("LRS", "GRS")),
    },
    execute=create_storage_account,
)
