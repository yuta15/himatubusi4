from collections.abc import Callable, Mapping
from dataclasses import dataclass
from types import MappingProxyType

from .models import Result
from .validation import Validator

type Executor = Callable[[Mapping[str, object]], Result]

_MISSING = object()


@dataclass(frozen=True)
class Field:
    validate: Validator
    default: object = _MISSING


@dataclass(frozen=True)
class ResourceSpec:
    fields: Mapping[str, Field]
    execute: Executor

    def __post_init__(self) -> None:
        object.__setattr__(self, "fields", MappingProxyType(dict(self.fields)))

    def validate(self, parameters: Mapping[str, object]) -> Mapping[str, object]:
        values = {}
        for name, field in self.fields.items():
            value = parameters.get(name, field.default)
            if value is _MISSING:
                raise ValueError(f"{name}: required")
            try:
                values[name] = field.validate(value)
            except ValueError as error:
                raise ValueError(f"{name}: {error}") from error
        return MappingProxyType(values)
