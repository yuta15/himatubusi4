from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import one_of, text


def create_app_service(values: Mapping[str, object]) -> Result:
    name = values["name"]
    plan_name = values["plan_name"]
    runtime = values["runtime"]

    # TODO: 以下のprintを、これらの引数でWeb Appを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "APP_SERVICE", {
        "name": name,
        "plan_name": plan_name,
        "runtime": runtime,
    }))
    return Result(True, f"Simulated web app creation: {name}")


SPEC = ResourceSpec(
    fields={
        "name": Field(text),
        "plan_name": Field(text),
        "runtime": Field(one_of("python", "node", "dotnet")),
    },
    execute=create_app_service,
)
