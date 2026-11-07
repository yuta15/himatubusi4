from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import text


def create_compute_engine(values: Mapping[str, object]) -> Result:
    name = values["name"]
    zone = values["zone"]
    machine_type = values["machine_type"]

    # TODO: 以下のprintを、これらの引数でCompute Engineインスタンスを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.GOOGLE_CLOUD, "COMPUTE_ENGINE", {
        "name": name,
        "zone": zone,
        "machine_type": machine_type,
    }))
    return Result(True, f"Simulated Compute Engine instance creation: {name}")


SPEC = ResourceSpec(
    fields={"name": Field(text), "zone": Field(text), "machine_type": Field(text)},
    execute=create_compute_engine,
)
