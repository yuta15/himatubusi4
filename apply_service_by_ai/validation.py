"""デモ用の検証。実クラウドの全制約を再現するものではない。"""

from collections.abc import Callable


type Validator = Callable[[object], object]


def text(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("must be a non-empty string")
    return value.strip()


def string_length(minimum: int, maximum: int) -> Callable[[object], str]:
    def validate(value: object) -> str:
        value = text(value)
        if not minimum <= len(value) <= maximum:
            raise ValueError(f"must contain {minimum} to {maximum} characters")
        return value

    return validate


def one_of(*options: str) -> Callable[[object], str]:
    def validate(value: object) -> str:
        value = text(value)
        if value not in options:
            raise ValueError(f"must be one of {options}")
        return value

    return validate


def integer(minimum: int, maximum: int, *, step: int = 1) -> Callable[[object], int]:
    def validate(value: object) -> int:
        if type(value) is not int or not minimum <= value <= maximum:
            raise ValueError(f"must be an integer between {minimum} and {maximum}")
        if value % step:
            raise ValueError(f"must be a multiple of {step}")
        return value

    return validate


def boolean(value: object) -> bool:
    if not isinstance(value, bool):
        raise ValueError("must be a boolean")
    return value


def http_url(value: object) -> str:
    value = text(value)
    if not value.startswith(("https://", "http://")):
        raise ValueError("must start with http:// or https://")
    return value


def hostname(value: object) -> str:
    value = text(value)
    if "://" in value or "/" in value or any(c.isspace() for c in value):
        raise ValueError("must be a hostname without a scheme or path")
    return value


def storage_account_name(value: object) -> str:
    value = string_length(3, 24)(value)
    if not value.isascii() or not value.isalnum() or value != value.lower():
        raise ValueError("must contain lowercase ASCII letters or digits")
    return value
