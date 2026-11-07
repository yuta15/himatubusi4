from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, text


def create_sns(values: Mapping[str, object]) -> Result:
    topic_name = values["topic_name"]
    region = values["region"]
    fifo = values["fifo"]

    # TODO: 以下のprintを、これらの引数でSNS topicを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "SNS", {
        "topic_name": topic_name,
        "region": region,
        "fifo": fifo,
    }))
    return Result(True, f"Simulated SNS topic creation: {topic_name}")


SPEC = ResourceSpec(
    fields={
        "topic_name": Field(text),
        "region": Field(text),
        "fifo": Field(boolean, default=False),
    },
    execute=create_sns,
)
