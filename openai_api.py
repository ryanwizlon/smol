import requests
import json

openai_api_key = "YOUR_OPENAI_API_KEY"

def api_get_request(prompt):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 60
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def get_response(prompt):
    response = api_get_request(prompt)
    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text'].strip()
    else:
        return "I'm sorry, I didn't understand that."