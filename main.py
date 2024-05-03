import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Define the path to the directory containing the model files
model_directory = "gemma-7b-it"

# Load the tokenizer and model from the local directory
tokenizer = AutoTokenizer.from_pretrained(model_directory)
model = AutoModelForCausalLM.from_pretrained(model_directory)

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
