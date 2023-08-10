```python
import json

def update_logs(session_data):
    with open('session_logs.json', 'r') as file:
        data = json.load(file)
        
    data.append(session_data)
    
    with open('session_logs.json', 'w') as file:
        json.dump(data, file)
```