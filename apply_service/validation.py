"""Builders用の入力検証。クラウドの厳密な仕様検証は扱わない。"""


def required_string(parameters: dict, key: str) -> str:
    value = parameters.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be a non-empty string")
    return value.strip()


def choice(parameters: dict, key: str, options: tuple[str, ...]) -> str:
    value = required_string(parameters, key)
    if value not in options:
        raise ValueError(f"{key} must be one of {options}")
    return value


def integer(parameters: dict, key: str, minimum: int, maximum: int) -> int:
    value = parameters.get(key)
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{key} must be an integer between {minimum} and {maximum}")
    return value


def boolean(parameters: dict, key: str, default: bool) -> bool:
    value = parameters.get(key, default)
    if not isinstance(value, bool):
        raise ValueError(f"{key} must be a boolean")
    return value
