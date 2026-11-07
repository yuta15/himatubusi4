from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import CloudFrontApplier


class CloudFrontBuilder(Builder):
    def build(self, request: Request) -> CloudFrontApplier:
        params = request.parameters
        distribution_name = required_string(params, "distribution_name")
        raw_origins = params.get("origins")
        if not isinstance(raw_origins, list) or not raw_origins:
            raise ValueError("origins must be a non-empty list")

        origins = []
        origin_ids = set()
        for index, origin in enumerate(raw_origins):
            if not isinstance(origin, dict):
                raise ValueError(f"origins[{index}] must be an object")
            origin_id = required_string(origin, "id")
            if origin_id in origin_ids:
                raise ValueError(f"origins contains duplicate id: {origin_id}")
            domain = required_string(origin, "domain")
            if "://" in domain or "/" in domain or any(c.isspace() for c in domain):
                raise ValueError(f"origins[{index}].domain must be a hostname without a scheme or path")
            validated_origin = {"id": origin_id, "domain": domain}
            if "path" in origin:
                path = origin["path"]
                if not isinstance(path, str) or not path.startswith("/"):
                    raise ValueError(f"origins[{index}].path must be a string starting with /")
                validated_origin["path"] = path
            origins.append(validated_origin)
            origin_ids.add(origin_id)

        default_origin_id = required_string(params, "default_origin_id")
        if default_origin_id not in origin_ids:
            raise ValueError("default_origin_id must match an id in origins")
        return CloudFrontApplier(
            distribution_name, origins, default_origin_id, boolean(params, "enabled", True),
        )

