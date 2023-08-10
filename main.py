```python
import json
from chatbot import ChatBot
from update_logs import update_logs

def main():
    # Initialize the chatbot
    chatbot = ChatBot()

    while True:
        # Get user input
        user_input = input("You: ")

        # If the user types 'quit', end the session
        if user_input.lower() == 'quit':
            break

        # Get the chatbot's response
        response = chatbot.get_response(user_input)

        # Print the chatbot's response
        print("ChatBot: " + response)

        # Update the session logs
        update_logs(user_input, response)

    print("Session ended.")

if __name__ == "__main__":
    main()
```