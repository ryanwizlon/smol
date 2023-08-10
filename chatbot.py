```python
import json
from openai_api import get_response

class ChatBot:
    def __init__(self):
        self.session_logs = "session_logs.json"

    def chat(self, message):
        response = get_response(message)
        self.update_logs(message, response)
        return response

    def update_logs(self, message, response):
        try:
            with open(self.session_logs, 'r') as logs:
                data = json.load(logs)
        except FileNotFoundError:
            data = []

        data.append({
            "message": message,
            "response": response
        })

        with open(self.session_logs, 'w') as logs:
            json.dump(data, logs)
```