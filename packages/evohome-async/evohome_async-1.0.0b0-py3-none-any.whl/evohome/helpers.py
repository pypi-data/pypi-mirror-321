"""evohomeasync provides an async client for the Resideo TCC API."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, TypeVar

from .const import _DBG_DONT_OBFUSCATE, REGEX_EMAIL_ADDRESS

if TYPE_CHECKING:
    from collections.abc import Callable

_T = TypeVar("_T")


def obfuscate(value: bool | int | str) -> bool | int | str | None:
    if _DBG_DONT_OBFUSCATE:
        return value
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return 0
    if not isinstance(value, str):
        raise TypeError(f"obfuscate() expects bool | int | str, got {type(value)}")
    if REGEX_EMAIL_ADDRESS.match(value):
        return "******@obfuscated.com"
    return "********"


def camel_to_pascal(s: str) -> str:
    """Convert a camelCase string to PascalCase."""
    if " " in s:
        raise ValueError("Input string should not contain spaces")
    return s[:1].upper() + s[1:]


_STEP_1 = re.compile(r"(.)([A-Z][a-z]+)")
_STEP_2 = re.compile(r"([a-z0-9])([A-Z])")


def camel_to_snake(s: str) -> str:
    """Return a string converted from camelCase to snake_case."""
    if " " in s:
        raise ValueError("Input string should not contain spaces")
    return _STEP_2.sub(r"\1_\2", _STEP_1.sub(r"\1_\2", s)).lower()


def snake_to_camel(s: str) -> str:
    """Return a string converted from snake_case to camelCase."""
    if " " in s:
        raise ValueError("Input string should not contain spaces")
    components = s.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def noop(s: str) -> str:
    """Return a string unconverted."""
    return s


def _convert_keys(data: _T, fnc: Callable[[str], str]) -> _T:
    """Recursively convert all dict keys to snake_case (or CamelCase).

    Used after retrieving (or before sending) JSON via the vendor API.
    """

    if isinstance(data, list):
        return [_convert_keys(item, fnc) for item in data]  # type:ignore[return-value]

    if not isinstance(data, dict):
        return data

    return {fnc(k): _convert_keys(v, fnc) for k, v in data.items()}  # type:ignore[return-value]


_KEYS_TO_OBSCURE = (
    "name",
    "username",
    "firstname",
    "lastname",
    "streetAddress",
    "city",
    "postcode",
    "zipcode",
    "telephone",
    "securityQuestion1",
    "securityQuestion2",
    "securityQuestion3",
    "mac",
    "crc",
)


def obscure_secrets(data: _T) -> _T:
    """Recursively obsfucate all dict/list values that might be secrets.

    Used for logging JSON received from the vendor API.
    """

    def _obfuscate(key: str, val: bool | int | str) -> bool | int | str | None:
        if key not in _KEYS_TO_OBSCURE:
            return val
        if not isinstance(val, str):
            return obfuscate(val)
        if REGEX_EMAIL_ADDRESS.match(val):
            return "nobody@nowhere.com"
        if "name" in key:
            return val[:2].ljust(len(val), "*")
        return "".join("*" if char != " " else " " for char in val)

    if isinstance(data, str):
        return data  # type:ignore[return-value]

    if isinstance(data, list):
        return [obscure_secrets(item) for item in data]  # type:ignore[return-value]

    if not isinstance(data, dict):
        return data

    return {
        k: _obfuscate(k, v) if k in _KEYS_TO_OBSCURE else obscure_secrets(v)
        for k, v in data.items()
    }  # type:ignore[return-value]


def convert_keys_to_camel_case(data: _T) -> _T:
    """Recursively convert all dict keys from snake_case to camelCase.

    Used before sending JSON to the vendor API.
    """
    return _convert_keys(data, snake_to_camel)


def convert_keys_to_snake_case(data: _T) -> _T:
    """Recursively convert all dict keys from camelCase to snake_case.

    Used after retrieving JSON from the vendor API.
    """
    return _convert_keys(data, camel_to_snake)
