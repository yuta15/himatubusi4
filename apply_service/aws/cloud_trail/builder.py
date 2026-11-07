from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import CloudTrailApplier


class CloudTrailBuilder(Builder):
    def build(self, request: Request) -> CloudTrailApplier:
        params = request.parameters
        return CloudTrailApplier(
            required_string(params, "trail_name"),
            required_string(params, "bucket_name"),
            boolean(params, "multi_region", True),
        )

