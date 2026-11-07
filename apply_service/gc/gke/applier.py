from ...base import Applier
from ...common import Provider, Result


class GkeApplier(Applier):
    def __init__(
        self,
        cluster_name: str,
        location: str,
        node_count: int,
        private_cluster: bool,
    ) -> None:
        self.cluster_name = cluster_name
        self.location = location
        self.node_count = node_count
        self.private_cluster = private_cluster

    def apply(self) -> Result:
        self._print(
            Provider.GOOGLE_CLOUD,
            "GKE",
            cluster_name=self.cluster_name,
            location=self.location,
            node_count=self.node_count,
            private_cluster=self.private_cluster,
        )
        return Result(True, f"Simulated GKE cluster creation: {self.cluster_name}")
