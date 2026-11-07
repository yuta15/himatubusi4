from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import CloudStorageApplier


class CloudStorageBuilder(Builder):
    def build(self, request: Request) -> CloudStorageApplier:
        params = request.parameters
        return CloudStorageApplier(
            required_string(params, "bucket_name"),
            required_string(params, "location"),
            boolean(params, "versioning", False),
        )
