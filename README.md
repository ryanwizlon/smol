# Customer Chat Bot using OpenAI

This is a guide on how to develop and deploy the customer chat bot using OpenAI.

## Development

1. Clone the repository to your local machine.

2. Install the required dependencies by running `pip install -r requirements.txt`.

3. Set your OpenAI API key as an environment variable. This can be done by adding the following line to your `.bashrc` or `.bash_profile`:

    `export OPENAI_API_KEY='your-api-key'`

4. The main entry point of the application is `main.py`. This script initializes the chat bot and starts the chat session.

5. The `chatbot.py` file contains the ChatBot class which is responsible for handling the conversation with the user.

6. The `openai_api.py` file contains the functions for interacting with the OpenAI API.

7. The `self_improvement.py` file contains the functions for improving the bot based on the session logs.

8. The `session_logs.json` file contains the logs of each session. The bot uses these logs to improve itself.

## Deployment

1. Ensure that you have set your OpenAI API key as an environment variable.

2. Run `python main.py` to start the chat bot.

## Self Improvement

The bot improves itself by analyzing the logs of each session. After each session, the `update_logs()` function in `self_improvement.py` is called to update the `session_logs.json` file. The `improve_bot()` function is then called to improve the bot based on the updated logs.

For more information on how to improve the bot, refer to the `improvement_suggestions.md` file.