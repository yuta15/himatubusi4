from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import text


def create_ec2(values: Mapping[str, object]) -> Result:
    name = values["name"]
    region = values["region"]
    instance_type = values["instance_type"]

    # TODO: 以下のprintを、これらの引数でEC2 instanceを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "EC2", {
        "name": name,
        "region": region,
        "instance_type": instance_type,
    }))
    return Result(True, f"Simulated EC2 instance creation: {name}")


SPEC = ResourceSpec(
    fields={
        "name": Field(text),
        "region": Field(text),
        "instance_type": Field(text),
    },
    execute=create_ec2,
)
