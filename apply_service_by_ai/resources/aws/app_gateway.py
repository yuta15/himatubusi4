from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import http_url, integer, text


def create_app_gateway(values: Mapping[str, object]) -> Result:
    name = values["name"]
    target_url = values["target_url"]
    port = values["port"]

    # TODO: 以下のprintを、これらの引数でゲートウェイを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "APP_GATEWAY", {
        "name": name,
        "target_url": target_url,
        "port": port,
    }))
    return Result(True, f"Simulated gateway creation: {name}")


# 既存の登録名を維持したデモ用のゲートウェイ。
SPEC = ResourceSpec(
    fields={"name": Field(text), "target_url": Field(http_url), "port": Field(integer(1, 65535))},
    execute=create_app_gateway,
)
