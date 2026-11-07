from . import compute_engine, gke


RESOURCES = {
    "COMPUTE_ENGINE": compute_engine.SPEC,
    "GKE": gke.SPEC,
}

__all__ = ["RESOURCES"]
