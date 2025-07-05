# ${\textsf{\color{#C25A7C}🤖 Simple Student Chat Backend - Python WebSocket Server}}$ 

${\textsf{\color{#FFC0CB}(Real-time AI-powered chat server built with FastAPI + Socket.IO to support personalized conversations using Ollama (Llama 3).)}}$

The Student Chat Backend is the server-side component of a real-time educational chatbot system. It handles socket connections from the frontend client, routes user prompts to an AI model (via Ollama (locally installed)) and logs detailed chats to ClickHouse.

For the frontend client, kindly refer to [https://github.com/M-Nkirote/Student-Chat-Python-websocket-client](url).

## ${\textsf{\color{#C25A7C}Features}}$ 📋
* ⚡ FastAPI + Socket.IO WebSocket server
* 🤖 Integration with Ollama (Llama 3) for AI responses
* 🧠 Session-based logging
* 🗃️ ClickHouse storage for chat logs and summaries
* 🔒 Token-based user identity (via JWT)
* 🌐 CORS-enabled for frontend interaction

## ${\textsf{\color{#C25A7C}Project Structure}}$ 🗂️
```bash
.
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── clickhouse_client.py
    ├── main.py
    └── model_handler.py
```

## ${\textsf{\color{#C25A7C}Set Up}}$ 🛠️
### ${\textsf{\color{#FFC0CB}Prerequisites}}$
* Python 3.10+
* Ollama installed and running (ollama run llama3)
* ClickHouse server running locally or remotely
* virtualenv (recommended)

### ${\textsf{\color{#FFC0CB}Clone the Repo}}$
>`git clone git@github.com:M-Nkirote/Student-Chat-Python-websocket-server.git`
>
> `cd Student-Chat-Python-websocket-server`

### ${\textsf{\color{#FFC0CB}Set up virtual environment}}$
> `python3 -m venv venv`
>
> `source venv/bin/activate`

### ${\textsf{\color{#FFC0CB}Install dependencies}}$
> `pip install -r requirements.txt`

### ${\textsf{\color{#FFC0CB}To run main.py}}$
> `cd /Student-Chat-Python-websocket-client/src`
>
> `uvicorn main:socket_app --host 0.0.0.0 --port 8001`

Server will be available at: [http://localhost:8001](url)

### ${\textsf{\color{#FFC0CB}Usage}}$
When a user sends a prompt via the frontend:
*The prompt is routed to the server via WebSocket.
*The server logs the message in ClickHouse.
*Ollama processes the message using Llama 3.
*The AI response is returned and logged.
*A background process stores the conversation in Clickhouse as it happens

### ${\textsf{\color{#FFC0CB}Contributions}}$
Feel free to fork the repo, suggest improvements, or file issues.
