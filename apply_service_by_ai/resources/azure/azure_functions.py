from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import one_of, text


def create_azure_functions(values: Mapping[str, object]) -> Result:
    name = values["name"]
    runtime = values["runtime"]
    storage_account = values["storage_account"]

    # TODO: 以下のprintを、これらの引数でFunction Appを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "AZURE_FUNCTIONS", {
        "name": name,
        "runtime": runtime,
        "storage_account": storage_account,
    }))
    return Result(True, f"Simulated function app creation: {name}")


SPEC = ResourceSpec(
    fields={
        "name": Field(text),
        "runtime": Field(one_of("python", "node", "dotnet")),
        "storage_account": Field(text),
    },
    execute=create_azure_functions,
)
