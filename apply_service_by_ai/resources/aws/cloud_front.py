from collections.abc import Mapping

from ...models import Provider, Result
from ...output import format_resource
from ...resource import Field, ResourceSpec
from ...validation import boolean, hostname, text


def validate_origins(value: object) -> list[dict[str, str]]:
    if not isinstance(value, list) or not value:
        raise ValueError("must be a non-empty list")

    origins = []
    origin_ids = set()
    for index, origin in enumerate(value):
        if not isinstance(origin, Mapping):
            raise ValueError(f"[{index}]: must be an object")
        validated_origin = {}
        for name, validator in (("id", text), ("domain", hostname)):
            if name not in origin:
                raise ValueError(f"[{index}].{name}: required")
            try:
                validated_origin[name] = validator(origin[name])
            except ValueError as error:
                raise ValueError(f"[{index}].{name}: {error}") from error
        origin_id = validated_origin["id"]
        if origin_id in origin_ids:
            raise ValueError(f"[{index}].id: duplicate id: {origin_id}")
        if "path" in origin:
            path = origin["path"]
            if not isinstance(path, str) or not path.startswith("/"):
                raise ValueError(f"[{index}].path: must be a string starting with /")
            validated_origin["path"] = path
        origins.append(validated_origin)
        origin_ids.add(origin_id)
    return origins


def validate_default_origin(values: Mapping[str, object]) -> None:
    if not any(origin["id"] == values["default_origin_id"] for origin in values["origins"]):
        raise ValueError("default_origin_id: must match an id in origins")


def create_cloud_front(values: Mapping[str, object]) -> Result:
    distribution_name = values["distribution_name"]
    origins = values["origins"]
    default_origin_id = values["default_origin_id"]
    enabled = values["enabled"]

    # TODO: 以下のprintを、これらの引数でCloudFrontディストリビューションを作成するAPI呼び出しに置き換える。
    print(format_resource(Provider.AWS, "CLOUD_FRONT", {
        "distribution_name": distribution_name,
        "origins": origins,
        "default_origin_id": default_origin_id,
        "enabled": enabled,
    }))
    return Result(True, f"Simulated CloudFront distribution creation: {distribution_name}")


SPEC = ResourceSpec(
    fields={
        "distribution_name": Field(text),
        "origins": Field(validate_origins),
        "default_origin_id": Field(text),
        "enabled": Field(boolean, default=True),
    },
    execute=create_cloud_front,
    validate_values=validate_default_origin,
)
