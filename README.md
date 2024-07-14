# Telegram Chat Join Bot

This project is a Telegram bot that handles chat join requests. When a new user requests to join a chat, the bot approves the request and sends a welcome message to the chat.

## Features

- Approves new chat join requests
- Sends a welcome message to the chat
- Logs chat join requests and any errors that occur

## Prerequisites

Before running the bot, ensure you have the following installed:

- Python 3.7+
- `aiogram` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Nodik2006/Auto-Accept-User-Request-Bot-for-Telegram.git
    cd Auto-Accept-User-Request-Bot-for-Telegram
    ```

2. Install the required Python packages:

    ```bash
    pip install aiogram
    ```

3. Create a new bot on Telegram by talking to the [BotFather](https://t.me/BotFather) and obtain your API token.

4. Update the `API_TOKEN` variable in `mainv2.py` with your bot's API token:

    ```python
    API_TOKEN = 'your-telegram-bot-token'
    ```

## Usage

To run the bot, execute the following command:

```bash
python mainv2.py
```

The bot will start polling for updates and will handle chat join requests automatically.

## Logging
The bot uses Python's built-in logging module to log messages. Logs include information about chat join requests and any errors that occur.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License
This project is licensed under the MIT License.
