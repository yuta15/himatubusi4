from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import integer, text


def create_cosmos_db(values: Mapping[str, object]) -> Result:
    account_name = values["account_name"]
    database_name = values["database_name"]
    throughput = values["throughput"]

    # TODO: 以下のprintを、これらの引数でCosmos DBを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "COSMOS_DB", {
        "account_name": account_name,
        "database_name": database_name,
        "throughput": throughput,
    }))
    return Result(True, f"Simulated Cosmos DB creation: {database_name}")


SPEC = ResourceSpec(
    fields={
        "account_name": Field(text),
        "database_name": Field(text),
        "throughput": Field(integer(400, 10000, step=100)),
    },
    execute=create_cosmos_db,
)
