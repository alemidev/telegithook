from typing import Any
from os import path
from yaml import safe_load

strings = safe_load(path.join(path.dirname(__file__), "strings.yml"))


def get_string(key: str) -> Any:
    if key in strings:
        return strings[key]

    return "There is no string with the key %s" % key
