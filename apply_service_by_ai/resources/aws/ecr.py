from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, text


def create_ecr(values: Mapping[str, object]) -> Result:
    repository_name = values["repository_name"]
    region = values["region"]
    scan_on_push = values["scan_on_push"]

    # TODO: 以下のprintを、これらの引数でECR repositoryを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "ECR", {
        "repository_name": repository_name,
        "region": region,
        "scan_on_push": scan_on_push,
    }))
    return Result(True, f"Simulated ECR repository creation: {repository_name}")


SPEC = ResourceSpec(
    fields={
        "repository_name": Field(text),
        "region": Field(text),
        "scan_on_push": Field(boolean, default=True),
    },
    execute=create_ecr,
)
