import torch 
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name = "gp12"
model = GPT2LMHeadModel.from_pretrained(model_name) 
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model.eval()
def generate_response(prompt, max_length=50):
    input_ids=tokenizer.encode(prompt, return_tensors="pt", add_special_tokens=True)
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    response_ids=model.generate(input_ids, max_length=max_length, num_return_sequences=1,attention_mask=attention_mask)
    response_text=tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text

print("Chatbot: Hello! How can I assist you today? (Type 'exit' to end)")

while True:
    user_input=input("You")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    bot_response = generate_response(user_input)
    print("Chatbot:", bot_response)