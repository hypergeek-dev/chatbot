import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
tokenizer = AutoTokenizer.from_pretrained("google/gemma-1.1-7b-it", token=access_token)
model = AutoModelForCausalLM.from_pretrained("google/gemma-1.1-7b-it", token=access_token)

# Determine device
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)
model.to(device)

# Start conversation loop
while True:
    # Get user input
    user_input = input("You: ")

    # Tokenize user input
    input_ids = tokenizer.encode(user_input, return_tensors="pt").to(device)

    # Generate response
    outputs = model.generate(input_ids, max_length=1000, do_sample=True, temperature=0.7)

    # Decode and print response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Bot:", response)
