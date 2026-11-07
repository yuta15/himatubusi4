from ...base import Builder
from ...common import Request
from ...validation import required_string
from .applier import Ec2Applier


class Ec2Builder(Builder):
    def build(self, request: Request) -> Ec2Applier:
        params = request.parameters
        return Ec2Applier(
            required_string(params, "name"),
            required_string(params, "region"),
            required_string(params, "instance_type"),
        )
