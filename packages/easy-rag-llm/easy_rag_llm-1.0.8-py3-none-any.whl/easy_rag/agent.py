import requests
import numpy as np
from openai import OpenAI

class Agent:
    def __init__(self, model, open_api_key=None, deepseek_api_key=None, deepseek_base_url=None):
        self.model = model
        self.open_api_key = open_api_key
        self.deepseek_api_key = deepseek_api_key
        self.deepseek_base_url = deepseek_base_url
        self.last_prompt = None

    def default_query_embedding_fn(self, query, index_dim):
        return np.random.random(index_dim).astype(np.float32)

    def generate_response(self, resource, query, return_prompt=False):
        index, metadata = resource
        query_embedding = self.default_query_embedding_fn(query, index.d)
        distances, indices = index.search(query_embedding.reshape(1, -1), 3)
        TOP_K = 3

        if indices.size == 0 or len(indices[0]) == 0:
            raise ValueError("No relevant evidence found.")

        evidence = [metadata[idx] for idx in indices[0] if idx < len(metadata)]
        if not evidence:
            raise ValueError("No valid evidence found.")

        formatted_evidence = "\n".join(
            [f"File: {e['file_name']}, Page: {e['page_number']}, Text: {e['text']}" for e in evidence[:TOP_K]]
        )
        prompt = f"""
        System: The following is the most relevant information from the Knowledge for your query.
        Given format of the Knowledge is JSON with the following structure:
        {{
            "text": "string",
            "page_number": "integer",
            "file_name": "string"
        }}
        Always answer in the same language as the User prompt and strictly based on the provided Knowledge.
        Do not speculate or create information beyond what is given.
        ==== Knowledge: start ====
        {formatted_evidence}
        ==== Knowledge: end ====

        User: Below is the User prompt:
        ==== User prompt: start ====
        {query}
        ==== User prompt: end ====
        """
        self.last_prompt = prompt.strip()
        if return_prompt:
            print(prompt)
            return self.last_prompt

        if self.deepseek_api_key:
            headers = {
                "Authorization": f"Bearer {self.deepseek_api_key}",
                "Content-Type": "application/json",
            }
            try:
                client = OpenAI(api_key=self.deepseek_api_key, base_url=self.deepseek_base_url)
                response = client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "system", "content": self.last_prompt}],
                    stream=False
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"Error while calling DeepSeek API: {e}")
                raise RuntimeError("DeepSeek API call failed.") from e

        return "DeepSeek API key not provided. Returning prompt only."

