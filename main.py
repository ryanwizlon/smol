import json
from chatbot import ChatBot
from openai_api import OpenAI_API
from self_improvement import SelfImprovement

openai_api_key = "YOUR_OPENAI_API_KEY"
session_logs = "session_logs.json"

def update_logs(session_data):
    with open(session_logs, 'a') as f:
        json.dump(session_data, f)

def main():
    chatbot = ChatBot(openai_api_key)
    openai_api = OpenAI_API(openai_api_key)
    self_improvement = SelfImprovement(session_logs)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        response = chatbot.get_response(user_input)
        print("ChatBot: ", response)

        session_data = {
            "user_input": user_input,
            "bot_response": response
        }
        update_logs(session_data)

        self_improvement.improve_bot()

if __name__ == "__main__":
    main()