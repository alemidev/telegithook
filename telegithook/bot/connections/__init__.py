from typing import List

from motor.motor_asyncio import AsyncIOMotorClient

from ...env import MONGO_URI


class Connections:
    def __init__(self):
        self.collection = AsyncIOMotorClient(MONGO_URI).telegithook.repos

    async def get(self, repo: str) -> List[int]:
        find = await self.collection.find_one(
            {
                'repo': repo,
            },
        )
        if find:
            return find['chats']
        return []

    async def add(self, repo: str, chat_id: int) -> bool:
        chats = await self.get(repo)
        if chat_id not in chats:
            chats.append(chat_id)
            await self.collection.update_one(
                {
                    'repo': repo,
                },
                {
                    '$set': {
                        'chats': chats,
                    },
                },
                upsert=True,
            )
            return True
        return False

    async def remove(self, repo: str):
        await self.collection.delete_one(
            {
                'repo': repo,
            },
        )


CONNECTIONS = Connections()
