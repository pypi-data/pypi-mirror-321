# easy_rag
### NOT YET ALLOWED.
### PLAN TO APPLY OPENAI AND DEEPSEEK MODELS.
## Usage
#### Install
```bash
pip install easy_rag
```

#### How to integrate to your service?
```python
from easy_rag import RagService

# Step 1: 서비스 초기화
rs = RagService( 
	embedding_model="text-embedding-3-small", # Fix openai.
	response_model="deepseek", # openai or deepseek
	open_api_key="your_openai_api_key_here",
	deepseek_api_key="your_deepseek_api_key_here",
	deepseek_base_url="https://api.deepseek.com", 
)

# Step 2: 자료 학습
# rsc()는 학습 리소스를 반환하며, 내부적으로 임베딩을 생성하고 저장
resource = rs.rsc("./rscFiles")  # rscFiles 디렉토리 아래 모든 파일 학습

# Step 3: 에이전트 생성 및 쿼리
# agent()는 입력 쿼리에 대한 답변을 생성
query = "What is the summary of the first document?"
response = rs.agent(resource, query)

print(response)
```

### MEMO.
pdf 제목을 강제하자. info.json 을 추가하는 방식 대신 pdf의 제목을 추출하는 방식으로.
worker 개수 사용자 단에서 조정할 필요성. 아니면 그냥 CPU 개수로 조절하는 방식 생각.
