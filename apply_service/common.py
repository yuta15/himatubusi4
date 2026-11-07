from enum import StrEnum
from dataclasses import dataclass


class Provider(StrEnum):
    AWS = "AWS"
    AZURE = "AZURE"
    GOOGLE_CLOUD = "GOOGLE_CLOUD"


@dataclass
class Request:
    provider:Provider
    resource_type: str
    parameters: dict


@dataclass
class Result:
    result:bool
    message: str
