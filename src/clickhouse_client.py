from clickhouse_connect import get_client
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

client = get_client(
    host=os.getenv("CLICKHOUSE_HOST"),
    username=os.getenv("CLICKHOUSE_USERNAME"),
    password=os.getenv("CLICKHOUSE_PASSWORD"),
    database=os.getenv("CLICKHOUSE_DATABASE"))


def insert_chat_message(code, first_name, session_code, speaker, message):
    created_at = datetime.utcnow()
    client.insert(
        'detailed_chat_logs',
        [
            (code, first_name, session_code, speaker, message, created_at)
        ],
        column_names=['code', 'first_name', 'session_code', 'speaker', 'message', 'created_at']
    )
