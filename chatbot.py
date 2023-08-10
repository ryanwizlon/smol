```python
import json
import openai_api
import self_improvement

class ChatBot:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        self.session_logs = []

    def get_response(self, message):
        response = openai_api.api_get_request(self.openai_api_key, message)
        self.update_logs(message, response)
        return response

    def update_logs(self, message, response):
        self.session_logs.append({
            "message": message,
            "response": response
        })
        with open('session_logs.json', 'w') as f:
            json.dump(self.session_logs, f)

    def improve_bot(self):
        self_improvement.improve_bot(self.session_logs)

if __name__ == "__main__":
    chatbot = ChatBot("your_openai_api_key_here")
    while True:
        message = input("You: ")
        response = chatbot.get_response(message)
        print("Bot: ", response)
        chatbot.improve_bot()
```