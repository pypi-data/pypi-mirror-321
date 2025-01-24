import faiss
import numpy as np
import os
from easy_rag.agent import Agent

from dotenv import load_dotenv

load_dotenv()

def test_agent():
    d = 128
    index = faiss.IndexFlatL2(d)
    data = np.random.random((10, d)).astype(np.float32)
    index.add(data)

    agent = Agent(
        model="openai",
        open_api_key=os.getenv("OPENAI_API_KEY"),
    )

    mock_resource = (index, [{"text": "Sample text", "file_name": "test.pdf", "page_number": i+1} for i in range(10)])
    query_embedding=data[0]
    query = "What is the content of test.pdf?"

    agent.default_query_embedding_fn = lambda query: query_embedding

    response = agent.generate_response(mock_resource, query)

    # 검증
    assert isinstance(response, str), "Response should be a string."
    assert "Sample text" in response, "Response should contain relevant information."
