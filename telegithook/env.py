from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
CHAT_ID = int(getenv('CHAT_ID'))
DEBUG = bool(getenv('DEBUG'))
EXCLUDE_EVENTS=list(map(str.lower, list(getenv('EXCLUDE_EVENTS').split())))