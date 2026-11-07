from ...base import Builder
from ...common import Request
from ...validation import integer, required_string
from .applier import VirtualMachineApplier


class VirtualMachineBuilder(Builder):
    def build(self, request: Request) -> VirtualMachineApplier:
        params = request.parameters
        return VirtualMachineApplier(
            required_string(params, "name"), required_string(params, "size"),
            integer(params, "disk_size_gb", 1, 1024),
        )

