# easy_rag_llm

## CAUTION
- easy-rag-llm==1.0.* version is testing version. These versions are usually invalid.

## 🇰🇷 소개
- easy_rag_llm는 OpenAI 및 DeepSeek 모델을 지원하는 간단한 RAG(정보 검색 및 생성) 기반 서비스를 제공합니다. 간단하게 RAG LLM을 서비스에 통합시킬 수 있도록 만들어졌습니다.
- (2025.01.15 기준/ v1.0.0) 학습가능한 자료 포맷은 PDF입니다.

## 🇺🇸 Introduction
- easy_rag_llm is a lightweight RAG-based service that supports both OpenAI and DeepSeek models.
It is designed to seamlessly integrate RAG-based LLM functionalities into your service.
- As of 2025-01-15 (v1.0.0), the supported resource format for training is PDF.

## Usage
#### Install
```bash
pip install easy_rag_llm
```

#### How to integrate to your service?
```python
from easy_rag import RagService

rs = RagService(
    embedding_model="text-embedding-3-small", #Fixed to OpenAI model
    response_model="deepseek-chat",  # Options: "openai" or "deepseek-chat"
    open_api_key="your_openai_api_key_here",
    deepseek_api_key="your_deepseek_api_key_here",
    deepseek_base_url="https://api.deepseek.com",
)

resource = rs.rsc("./rscFiles")  # Learn from all files under ./rscFiles

query = "What is the summary of the first document?"
response = rs.generate_response(resource, query)

print(response)
```

### 🇰🇷 메모.
pdf 제목을 명확하게 적어주세요. 메타데이터에는 pdf제목이 추출되어 들어가며, 답변 근거를 출력할때 유용하게 사용될 수 있습니다.  

### 🇺🇸 Memo.
- Ensure that your PDFs have clear titles. Extracted titles from the PDF metadata are used during training and for generating evidence-based responses.

### Author Information
- 곽병혁 (https://github.com/Aiden-Kwak)
