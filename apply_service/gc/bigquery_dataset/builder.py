from ...base import Builder
from ...common import Request
from ...validation import required_string
from .applier import BigQueryDatasetApplier


class BigQueryDatasetBuilder(Builder):
    def build(self, request: Request) -> BigQueryDatasetApplier:
        params = {"location": "asia-northeast1", **request.parameters}
        return BigQueryDatasetApplier(
            required_string(params, "dataset_id"),
            required_string(params, "project_id"),
            required_string(params, "location"),
        )
