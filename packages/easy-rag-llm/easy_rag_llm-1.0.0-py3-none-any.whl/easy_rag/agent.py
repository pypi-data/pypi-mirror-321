import requests
import numpy as np

class Agent:
    def __init__(self, model, open_api_key=None, deepseek_api_key=None, deepseek_base_url=None):
        self.model = model
        self.open_api_key = open_api_key
        self.deepseek_api_key = deepseek_api_key
        self.deepseek_base_url = deepseek_base_url
        
        self.default_query_embedding_fn=self.default_query_embedding_fn

    def default_query_embedding_fn(self, query): # Agent 단일 테스트용 임시 임베딩.
        return np.random.random(128).astype(np.float32) 

    def generate_response(self, resource, query):
        index, metadata = resource
        query_embedding = np.random.random(index.d).astype(np.float32)
        distances, indices = index.search(query_embedding.reshape(1, -1), 5)
        
        # Format evidence from metadata
        evidence = [metadata[idx] for idx in indices[0]]
        response = f"Top evidence for query '{query}':\n" + "\n".join(
            [f"File: {e['file_name']}, Page: {e['page_number']}, Text: {e['text']}" for e in evidence]
        )
        #print(response)
        return response
