import ollama
import asyncio
from clickhouse_client import insert_chat_message


def _blocking_ollama_chat(prompt: str):
    return ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful tutor assisting students with simple questions.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )


async def process_prompt(prompt: str, student_code: str, first_name: str, session_code: str):
    # Insert student prompt to DB
    insert_chat_message(student_code, first_name, session_code, "student", prompt)

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, _blocking_ollama_chat, prompt)
    model_response = response['message']['content'].strip()

    # Insert model response to DB
    insert_chat_message(student_code, first_name, session_code, "model", model_response)

    return model_response
