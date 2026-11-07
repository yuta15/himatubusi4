from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import text


def create_bigquery_dataset(values: Mapping[str, object]) -> Result:
    dataset_id = values["dataset_id"]
    project_id = values["project_id"]
    location = values["location"]

    # TODO: 以下のprintを、これらの引数でBigQuery datasetを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.GOOGLE_CLOUD, "BIGQUERY_DATASET", {
        "dataset_id": dataset_id,
        "project_id": project_id,
        "location": location,
    }))
    return Result(True, f"Simulated BigQuery dataset creation: {dataset_id}")


SPEC = ResourceSpec(
    fields={
        "dataset_id": Field(text),
        "project_id": Field(text),
        "location": Field(text, default="asia-northeast1"),
    },
    execute=create_bigquery_dataset,
)
