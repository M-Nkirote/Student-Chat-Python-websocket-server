from clickhouse_connect import get_client
from datetime import datetime

client = get_client(host='localhost', username='default', password='')


def insert_chat_message(code, first_name, session_code, speaker, message):
    created_at = datetime.utcnow()
    client.insert(
        'student_chat_python_websocket.detailed_chat_logs',
        [
            (code, first_name, session_code, speaker, message, created_at)
        ],
        column_names=['code', 'first_name', 'session_code', 'speaker', 'message', 'created_at']
    )
