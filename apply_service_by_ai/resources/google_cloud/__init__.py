from . import artifact_registry, secret_manager, bigquery_dataset
from . import compute_engine, gke, cloud_storage, pub_sub, cloud_run


RESOURCES = {
    "COMPUTE_ENGINE": compute_engine.SPEC,
    "GKE": gke.SPEC,
    "CLOUD_STORAGE": cloud_storage.SPEC,
    "PUB_SUB": pub_sub.SPEC,
    "CLOUD_RUN": cloud_run.SPEC,
    "ARTIFACT_REGISTRY": artifact_registry.SPEC,
    "SECRET_MANAGER": secret_manager.SPEC,
    "BIGQUERY_DATASET": bigquery_dataset.SPEC,
}

__all__ = ["RESOURCES"]
