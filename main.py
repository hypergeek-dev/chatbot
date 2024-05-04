import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

# Load pre-trained model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct", 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True, 
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")

# Define conversation function
def chat():
    # Initialize conversation pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )
    
    # Start conversation loop
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to end the conversation
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        
        # Generate response based on user input
        output = pipe([{"role": "user", "content": user_input}], 
                      max_new_tokens=150, 
                      temperature=0.7)
        
        # Print assistant's response
        print("Assistant:", output[0]['generated_text'][1]['content'])
# Start the conversation
chat()
