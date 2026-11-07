from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum


class Provider(StrEnum):
    AWS = "AWS"
    AZURE = "AZURE"
    GOOGLE_CLOUD = "GOOGLE_CLOUD"


@dataclass(frozen=True)
class Request:
    provider: Provider
    resource_type: str
    parameters: Mapping[str, object]


@dataclass(frozen=True)
class Result:
    result: bool
    message: str
