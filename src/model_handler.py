import ollama
import asyncio


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


async def process_prompt(prompt: str, student_code: str):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, _blocking_ollama_chat, prompt)
    return f"{response['message']['content'].strip()}"
