from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, integer, text


def create_gke(values: Mapping[str, object]) -> Result:
    cluster_name = values["cluster_name"]
    location = values["location"]
    node_count = values["node_count"]
    private_cluster = values["private_cluster"]

    # TODO: 以下のprintを、これらの引数でGKEクラスタを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.GOOGLE_CLOUD, "GKE", {
        "cluster_name": cluster_name,
        "location": location,
        "node_count": node_count,
        "private_cluster": private_cluster,
    }))
    return Result(True, f"Simulated GKE cluster creation: {cluster_name}")


SPEC = ResourceSpec(
    fields={
        "cluster_name": Field(text),
        "location": Field(text),
        "node_count": Field(integer(1, 100)),
        "private_cluster": Field(boolean, default=False),
    },
    execute=create_gke,
)
