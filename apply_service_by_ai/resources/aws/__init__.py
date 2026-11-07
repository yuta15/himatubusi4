from . import s3, app_gateway, cloud_front, cloud_trail


RESOURCES = {
    "S3": s3.SPEC,
    "APP_GATEWAY": app_gateway.SPEC,
    "CLOUD_FRONT": cloud_front.SPEC,
    "CLOUD_TRAIL": cloud_trail.SPEC,
}

__all__ = ["RESOURCES"]
