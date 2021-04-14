import typing
import os
import yaml


class String:
    def __init__(self, data: typing.Union[dict, str]):
        self.data = data

    def __call__(self):
        return self.data

    def __getattr__(self, name: str):
        if isinstance(self.data, dict):
            if name in self.data:
                return String(self.data[name])

    def __getitem__(self, name: str):
        if isinstance(self.data, dict):
            if name in self.data:
                return String(self.data[name])


class Strings:
    def __init__(self, _file: str = os.path.join(os.path.dirname(__file__), 'strings.yml')):
        self._file = _file
        self._strings = {}
        self.reload_strings()

    def reload_strings(self):
        with open(self._file) as f:
            self._strings = yaml.safe_load(f.read())

    def get(self, key: str, parent: str = None):
        if parent:
            if parent in self._strings:
                return String(self._strings[parent])[key]
        else:
            if key in self._strings:
                return String(self._strings[key])

    def action(self, key: str):
        return self.get(key, 'actions')
