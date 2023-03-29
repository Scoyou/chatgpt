# ChatGPT-CLI

ChatGPT-CLI is a command-line interface (CLI) app that uses the ChatGPT chat collection to provide chatbot conversations in the terminal.

## Features

- Provides chatbot conversations using the ChatGPT chat collection
- Easy to use command-line interface
- Responses appear in the terminal
- Messages between user and chatGPT are persisted in a Mongodb database
    - Messages can be deleted anytime by typing 'delete all messages'

## Installation

1. Clone the repository from GitHub:

   ```
   git clone https://github.com/Scoyou/chatgpt-cli.git
   ```

2. Install the required packages using pip:

   ```
   pip install -r requirements.txt
   ```

3. Add your ChatGPT API key as an env variable:

    ``` 
    export OPENAI_API_KEY=yourapikey
    ```

4. Make file executable:

    ```
    chmod +x main.py
    ```

## Usage

1. Ask a question by typing the following command in your terminal:

   ```
   chatgpt/main.py Hello world, how are you today
   ```

2. The chatbot will respond in the terminal with its answer:

   ```
   >>> Hello! How can I help you today?
   ```

   You can continue the conversation by repating step one.

## Contributing

If you want to contribute to the project, you can fork the repository on GitHub and create a pull request. You can also create issues for bugs or feature requests.
