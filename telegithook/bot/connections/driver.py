import os
import sqlite3

from typing import Union, List

HERE = os.path.dirname(__file__)

class Driver:
    """A wrapper around a sqlite3 db with just 1 table holding 
       a one-to-many relation: username/repo -> chat_id"""
    def __init__(self, name="conn.db"):
        self.db = sqlite3.connect(os.path.join(HERE, name))
        tables = self.db.cursor().execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        if not any(res[0] == "connections" for res in tables):
            self.db.cursor().execute("CREATE TABLE connections(repo VARCHAR(255), chat_id INT);")
     
    def query(self, base:str, *replaces, flat=False):
        """Handy, query manually for iterations, commit if making edits!"""
        res = self.db.cursor().execute(base, replaces).fetchall()
        if flat:
            return [ el for row in res for el in row ]
        return res

    def all(self):
        """Get all relations"""
        return self.query("SELECT * FROM connections")

    def get(self, repo:str) -> List[int]:
        """Get list of chat_ids associated to one repo"""
        assert len(repo) < 255
        return self.query("SELECT chat_id FROM connections WHERE repo = ?", repo, flat=True) 

    def get_repos(self, chat_id:int) -> List[int]:
        """Get all repos associated to one chat_id"""
        return self.query("SELECT repo FROM connections WHERE chat_id = ?", chat_id, flat=True)

    def add(self, repo:str, chat_id:int) -> bool:
        """Add one repo:chat_id row. Will check if already present and return false if not added"""
        assert len(repo) < 255
        if chat_id in self.get(repo):
            return False
        with self.db:
            self.query("INSERT INTO connections VALUES (?, ?);", repo, chat_id)
            self.db.commit()
        return True

    def remove(self, repo:str, chat_id:int):
        """Will remove one row repo:chat_id if present"""
        assert len(repo) < 255
        with self.db:
            self.query("DELETE FROM connections WHERE repo = ? AND chat_id = ?", repo, chat_id)
            self.db.commit()

    def remove_all(self, repo:str):
        """Will remove all rows associated to a repo if present"""
        assert len(repo) < 255
        with self.db:
            self.query("DELETE FROM connections WHERE repo = ?", repo)
            self.db.commit()

    def remove_all_chats(self, chat_id:int):
        """Will remove all rows associated to a chat_id if present"""
        with self.db:
            self.query("DELETE FROM connections WHERE chat_id = ?", repo)
            self.db.commit()

DB = Driver()