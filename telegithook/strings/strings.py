from typing import Any
from os import path
from yaml import safe_load

with open(path.join(path.dirname(__file__), "strings.yml")) as f:
    STRINGS = safe_load(f)


def get_string(key: str) -> str: # this doesn't allow nested entries, needs to be recursive or just use builtin dict
    if key in strings:
        return STRINGS["actions"][key]
    raise KeyError("There is no string with the key %s" % key)
