from collections.abc import Mapping

from .models import Provider


def format_resource(provider: Provider, resource_type: str, values: Mapping[str, object]) -> str:
    width = max((len(key) for key in values), default=0)
    lines = [f"[{provider}/{resource_type}]"]
    lines.extend(f"  {key:<{width}} : {value}" for key, value in values.items())
    return "\n".join(lines)
