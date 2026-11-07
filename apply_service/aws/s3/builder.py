from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import S3Applier


class S3Builder(Builder):
    def build(self, request: Request) -> S3Applier:
        params = request.parameters
        name = required_string(params, "bucket_name")
        if not 3 <= len(name) <= 63:
            raise ValueError("bucket_name must contain 3 to 63 characters")
        return S3Applier(name, required_string(params, "region"), boolean(params, "versioning", False))

