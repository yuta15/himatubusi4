from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import integer, text


def create_sqs(values: Mapping[str, object]) -> Result:
    queue_name = values["queue_name"]
    region = values["region"]
    visibility_timeout = values["visibility_timeout"]

    # TODO: 以下のprintを、これらの引数でSQS queueを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "SQS", {
        "queue_name": queue_name,
        "region": region,
        "visibility_timeout": visibility_timeout,
    }))
    return Result(True, f"Simulated SQS queue creation: {queue_name}")


SPEC = ResourceSpec(
    fields={
        "queue_name": Field(text),
        "region": Field(text),
        "visibility_timeout": Field(integer(0, 43200)),
    },
    execute=create_sqs,
)
