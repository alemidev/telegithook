"""
This is useless boilerplate. Literally making simple things difficult.
This may have sense if we can build autocompletion based off the yaml file,
but just like this it's awful, because it is just reinventing the wheel.
Python has dictionaries, why would we need a weird wrapper around a dictionary??
"""
import os
import yaml

from typing import Any, Union

def load_strings(fname : str = 'strings.yml') -> dict :
    if not fname.startswith("/"): # user gave relative path, join with current folder
        fname = os.path.join(os.path.dirname(__file__), fname)
    with open(fname) as f:
        return yaml.safe_load(f.read())

# This is kinda sketchy, just to allow static __getitem__!
class StringDictType(type): 
    """Classes having this as a type can statically be accessed as dictionaries,
       to directly explore the static strings loaded off yml"""
    data = load_strings()

    def __init__(cls, name, bases, dct):
        cls.data = self.data
    
    def __getitem__(cls, key:str) -> Any:
        return cls.data[key]
    
    def __setitem__(cls, key:str, value:Any): # strings shouldn't be editable
        raise NotImplementedError("It is not possible to modify static strings at runtime")
    
    def __delitem__(cls, key:str): # strings shouldn't be editable
        raise NotImplementedError("It is not possible to modify static strings at runtime")
    
    def __iter__(cls):
        return iter(cls.data)
    
    def __len__(cls):
        return len(cls.data)

class String(metaclass=Strings):
    """Getter for static strings. Define a string you need to access by attribute access:
            > commit_str = Getter().actions.commits.head
       This class can also be statically accessed as a dict to directly explore the static strings:
            > commit_str = Getter["action"]["commits"]["head"]
       This is mostly a convenience to make accessing static strings easier."""
    def __init__(self):
        self.value = Getter.data

    def __getattr__(self, name:str):
        self.value = self.value[name]
        return self

    def __len__(self):
        if type(self.value) is str:
            return 1
        return len(self.value)

    def get(self) -> Union[dict, str]:
        """Will return current held value. Navigate values with attribute access"""
        return self.value

