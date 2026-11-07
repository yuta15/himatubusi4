from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import text


def create_pub_sub(values: Mapping[str, object]) -> Result:
    topic_name = values["topic_name"]
    project_id = values["project_id"]

    # TODO: 以下のprintを、これらの引数でPub/Sub topicを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.GOOGLE_CLOUD, "PUB_SUB", {
        "topic_name": topic_name,
        "project_id": project_id,
    }))
    return Result(True, f"Simulated Pub/Sub topic creation: {topic_name}")


SPEC = ResourceSpec(
    fields={
        "topic_name": Field(text),
        "project_id": Field(text),
    },
    execute=create_pub_sub,
)
