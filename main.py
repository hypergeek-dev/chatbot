from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")

tokenizer = AutoTokenizer.from_pretrained("google/gemma-1.1-7b-it", token=access_token)
model = AutoModelForCausalLM.from_pretrained("google/gemma-1.1-7b-it", token=access_token)

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)
model.to(device)

def generate_responses(user_inputs):
    input_ids_list = [tokenizer.encode(input_text, return_tensors="pt").to(device) for input_text in user_inputs]
    max_length = max(len(input_ids[0]) for input_ids in input_ids_list)
    input_ids_list = [torch.nn.functional.pad(input_ids, (0, max_length - input_ids.shape[1])) for input_ids in input_ids_list]
    input_ids = torch.stack(input_ids_list)
    outputs = model.generate(input_ids, max_length=1000, do_sample=True, temperature=0.7)
    responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return responses

while True:
    user_inputs = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        user_inputs.append(user_input)

    responses = generate_responses(user_inputs)

    for response in responses:
        print("Bot:", response)
