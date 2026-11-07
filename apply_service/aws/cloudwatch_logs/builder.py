from ...base import Builder
from ...common import Request
from ...validation import integer, required_string
from .applier import CloudWatchLogsApplier


class CloudWatchLogsBuilder(Builder):
    def build(self, request: Request) -> CloudWatchLogsApplier:
        params = {"retention_days": 30, **request.parameters}
        return CloudWatchLogsApplier(
            required_string(params, "log_group_name"),
            required_string(params, "region"),
            integer(params, "retention_days", 1, 365),
        )
