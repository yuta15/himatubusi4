from ...base import Builder
from ...common import Request
from ...validation import choice, required_string
from .applier import StorageAccountApplier


class StorageAccountBuilder(Builder):
    def build(self, request: Request) -> StorageAccountApplier:
        params = request.parameters
        name = required_string(params, "account_name")
        if not 3 <= len(name) <= 24 or not name.isascii() or not name.isalnum() or name != name.lower():
            raise ValueError("account_name must contain 3 to 24 lowercase ASCII letters or digits")
        return StorageAccountApplier(
            name, required_string(params, "location"), choice(params, "replication", ("LRS", "GRS"))
        )

