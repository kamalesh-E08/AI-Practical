from transformers import BertTokenizer, BertModel 
import torch 
from sklearn.metrics.pairwise import cosine_similarity

tokenizer=BertTokenizer.from_pretrained("bert-base-uncased")
model =BertModel.from_pretrained("bert-base-uncased") 
documents = [
"I want to book a flight from New York to London.",
"How can I reserve a flight from London to New York?",
"Tell me about flight booking options.",
"What's the procedure to purchase airline tickets?",
]

user_query= "Find me a flight from New York to London."

def preprocess(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True) 
    return inputs

user_query_inputs = preprocess(user_query)

document_embeddings = [preprocess(doc) for doc in documents]

similarities = [] 
with torch.no_grad():
    user_query_embedding = model(user_query_inputs).pooler_output
    for doc_embedding_inputs in document_embeddings:
        doc_embedding = model(**doc_embedding_inputs).pooler_output
        similarity=cosine_similarity(user_query_embedding, doc_embedding)
        similarities.append(similarity.item())

most_similar_index = similarities.index(max(similarities))
print("User Query:", user_query)
print("Most Similar Document:", documents[most_similar_index])