# Chatbot

## Introduction
This chatbot utilizes Hugging Face and Gemma data model. Gemma is a family of lightweight, state-of-the-art open models built from the same research and technology used to create the Gemini models. Developed by Google DeepMind and other teams across Google, Gemma is named after the Latin gemma, meaning "precious stone." The Gemma model weights are supported by developer tools that promote innovation, collaboration, and the responsible use of artificial intelligence (AI).

## Features
- Conversational AI
- Audio response
- Multimodal search

## Usage
1. Install dependencies:
    ```bash
    pip install transformers torch python-dotenv
    ```

2. Create a `.env` file in the project directory and add your access token:
    ```
    ACCESS_TOKEN=your_access_token_here
    ```

3. Run the script:
    ```bash
    python chatbot.py
    ```

4. Start interacting with the chatbot. Type your messages and press Enter. To exit the conversation, type "exit" and press Enter.

NB. This is a product in the making and has not yet been fine-tuned for local use. Response time might be slow.