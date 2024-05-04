# Phi-3-mini Chatbot

## Introduction
We introduce phi-3-mini, a 3.8 billion parameter language model trained on 3.3 trillion tokens, whose overall performance, as measured by both academic benchmarks and internal testing, rivals that of models such as Mixtral 8x7B and GPT-3.5 (e.g., phi-3-mini achieves 69% on MMLU and 8.38 on MT-bench), despite being small enough to be deployed on a phone. The innovation lies entirely in our dataset for training, a scaled-up version of the one used for phi-2, composed of heavily filtered web data and synthetic data. The model is also further aligned for robustness, safety, and chat format. We also provide some initial parameter-scaling results with a 7B and 14B models trained for 4.8T tokens, called phi-3-small and phi-3-medium, both significantly more capable than phi-3-mini (e.g., respectively 75% and 78% on MMLU, and 8.7 and 8.9 on MT-bench).


## Features
- Conversational AI
- Audio response
- Multimodal search

## Usage
1. Install dependencies:
    ```bash
    pip install transformers
    ```

2. Clone the `microsoft/Phi-3-mini-128k-instruct` model from the Hugging Face model hub:
    ```bash
    git clone https://huggingface.co/microsoft/Phi-3-mini-128k-instruct

3. Run the script:
    ```bash
    python main.py
    ```

4. Start interacting with the chatbot. Type your messages and press Enter. To exit the conversation, type "exit" and press Enter.

