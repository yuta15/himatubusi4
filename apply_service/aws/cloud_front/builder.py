from ...base import Builder
from ...common import Request
from ...validation import boolean, required_string
from .applier import CloudFrontApplier


class CloudFrontBuilder(Builder):
    def build(self, request: Request) -> CloudFrontApplier:
        params = request.parameters
        domain = required_string(params, "origin_domain")
        if "://" in domain or "/" in domain or any(c.isspace() for c in domain):
            raise ValueError("origin_domain must be a hostname without a scheme or path")
        return CloudFrontApplier(domain, boolean(params, "enabled", True))

