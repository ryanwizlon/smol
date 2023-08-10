```python
import os
import requests
import json

def get_response(message):
    API_KEY = os.getenv('API_KEY')
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'prompt': message,
        'max_tokens': 60
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    return response_json['choices'][0]['text'].strip()
```