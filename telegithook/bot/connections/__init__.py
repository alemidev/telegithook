import os
import json

class Connections:
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), 'connections.json')
        self.load_data()

    def load_data(self):
        try:
            with open(self.path) as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
            self.serialize_data()

    def serialize_data(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f)

    def get(self, repo:str) -> list[int]:
        if repo in self.data:
            return self.data[repo]
        return []

    def add(self, repo:str, chat_id:int):
        if repo not in self.data:
            self.data[repo] = []
        self.data[repo].append(chat_id)
        self.serialize_data()

    def remove(self, repo:str) -> bool:
        if repo in self.data and self.data.pop(repo):
            return True
        return False


CONNECTIONS = Connections()
