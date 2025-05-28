import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "10768857"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "81b5d675d410f16ceb39df10db9cdb54")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8122988957:AAG91AJVb5VefW1n4I-2OChf00TIjgkzsso")

OWNER_ID = int(os.environ.get("OWNER_ID", "6520378417"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002631081956"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "1002631081956")  # Optional here you'll get all logs
