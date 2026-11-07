from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import text


def create_secrets_manager(values: Mapping[str, object]) -> Result:
    secret_name = values["secret_name"]
    region = values["region"]

    # TODO: 以下のprintを、これらの引数でSecrets Manager secretを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "SECRETS_MANAGER", {
        "secret_name": secret_name,
        "region": region,
    }))
    return Result(True, f"Simulated Secrets Manager secret creation: {secret_name}")


SPEC = ResourceSpec(
    fields={
        "secret_name": Field(text),
        "region": Field(text),
    },
    execute=create_secrets_manager,
)
