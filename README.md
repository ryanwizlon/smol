# OpenAI Customer Chatbot

This is a simple interface for creating a customer chatbot using OpenAI. The chatbot is self-improving through updates to its own .json logs detailing each session.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to install the software specified in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Environment Variables

You need to set the following environment variable:

- `API_KEY`: Your OpenAI API key.

### Running the Application

To run the application, execute the following command:

```bash
python main.py
```

## Files

- `main.py`: This is the main file that runs the application.
- `chatbot.py`: This file contains the `chatbot` class that handles chatbot interactions.
- `openai_api.py`: This file contains the `get_response` function that interacts with the OpenAI API.
- `update_logs.py`: This file contains the `update_logs` function that updates the chatbot's session logs.
- `session_logs.json`: This file stores the chatbot's session logs.
- `improvement_suggestions.md`: This file contains suggestions on how to improve the application.

## Development

For development purposes, you can make changes to the `chatbot.py`, `openai_api.py`, and `update_logs.py` files. After making changes, you can run the application using the command specified in the "Running the Application" section.

## Deployment

To deploy the application, you can use any cloud platform that supports Python applications. You need to set the environment variable and install the prerequisites specified in the "Prerequisites" and "Environment Variables" sections.

## Contributing

As this application is intended for personal use, contributions are not currently accepted. However, you can refer to the `improvement_suggestions.md` file for ideas on how to improve the application.

## License

This project is licensed under the MIT License.