import requests
import numpy as np

class Agent:
    def __init__(self, model, open_api_key=None, deepseek_api_key=None, deepseek_base_url=None):
        self.model = model
        self.open_api_key = open_api_key
        self.deepseek_api_key = deepseek_api_key
        self.deepseek_base_url = deepseek_base_url
        
        #self.default_query_embedding_fn=self.default_query_embedding_fn

    def default_query_embedding_fn(self, query): # Agent 단일 테스트용 임시 임베딩.
        return np.random.random(self.index.d).astype(np.float32) 

    def generate_response(self, resource, query):
        index, metadata = resource
        query_embedding = self.default_query_embedding_fn(query)
        distances, indices = index.search(query_embedding.reshape(1, -1), 5)

        if indices.size == 0 or len(indices[0]) == 0:
            raise ValueError("No relevant evidence found.")

        evidence = [metadata[idx] for idx in indices[0] if idx < len(metadata)]
        if not evidence:
            raise ValueError("No valid evidence found.")

        formatted_evidence = "\n".join(
            [f"File: {e['file_name']}, Page: {e['page_number']}, Text: {e['text']}" for e in evidence]
        )
        response = f"Top evidence for query '{query}':\n{formatted_evidence}"

        if self.deepseek_api_key:
            prompt = query
            headers = {
                "Authorization": f"Bearer {self.deepseek_api_key}",
                "Content-Type": "application/json",
            }
            try:
                api_response = requests.post(
                    url=f"{self.deepseek_base_url}/chat/completions",
                    headers=headers,
                    json={
                        "model": self.model,
                        "messages": [{"role": "system", "content": prompt}],
                    }
                )
                api_response.raise_for_status()
                data = api_response.json()
                if "choices" not in data or not data["choices"]:
                    raise ValueError("Invalid response format from DeepSeek API")
                return data["choices"][0]["message"]["content"]
            except requests.exceptions.RequestException as e:
                print(f"Error while calling DeepSeek API: {e}")
                raise RuntimeError(f"Error while calling DeepSeek API: {e}")
            except ValueError as e:
                print(f"Error while processing DeepSeek API response: {e}")
                raise RuntimeError(f"Error while processing DeepSeek API response: {e}")

        return response
