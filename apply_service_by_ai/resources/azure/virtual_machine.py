from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import integer, text


def create_virtual_machine(values: Mapping[str, object]) -> Result:
    name = values["name"]
    size = values["size"]
    disk_size_gb = values["disk_size_gb"]

    # TODO: 以下のprintを、これらの引数で仮想マシンを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AZURE, "VIRTUAL_MACHINE", {
        "name": name,
        "size": size,
        "disk_size_gb": disk_size_gb,
    }))
    return Result(True, f"Simulated virtual machine creation: {name}")


SPEC = ResourceSpec(
    fields={"name": Field(text), "size": Field(text), "disk_size_gb": Field(integer(1, 1024))},
    execute=create_virtual_machine,
)
