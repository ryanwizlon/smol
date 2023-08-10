import json
from chatbot import ChatBot

def update_logs(session_logs, session):
    with open('session_logs.json', 'r+') as file:
        data = json.load(file)
        data[session_logs].append(session)
        file.seek(0)
        json.dump(data, file)

def improve_bot(chatbot, session_logs):
    with open('session_logs.json', 'r') as file:
        data = json.load(file)
        for session in data[session_logs]:
            chatbot.learn(session)

if __name__ == "__main__":
    chatbot = ChatBot()
    session_logs = "session_logs"
    session = {"session_id": 1, "user_input": "Hello", "bot_response": "Hi, how can I help you?"}
    update_logs(session_logs, session)
    improve_bot(chatbot, session_logs)