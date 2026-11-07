from ...base import Builder
from ...common import Request
from ...validation import integer, required_string
from .applier import LogAnalyticsApplier


class LogAnalyticsBuilder(Builder):
    def build(self, request: Request) -> LogAnalyticsApplier:
        params = {"retention_days": 30, **request.parameters}
        return LogAnalyticsApplier(
            required_string(params, "workspace_name"),
            required_string(params, "location"),
            integer(params, "retention_days", 30, 730),
        )
