from .resource import Field, ResourceSpec, simulated
from .validation import boolean, integer, text


RESOURCES = {
    "COMPUTE_ENGINE": ResourceSpec(
        fields={"name": Field(text), "zone": Field(text), "machine_type": Field(text)},
        execute=simulated("Simulated Compute Engine instance creation: {name}"),
    ),
    "GKE": ResourceSpec(
        fields={
            "cluster_name": Field(text),
            "location": Field(text),
            "node_count": Field(integer(1, 100)),
            "private_cluster": Field(boolean, default=False),
        },
        execute=simulated("Simulated GKE cluster creation: {cluster_name}"),
    ),
}
