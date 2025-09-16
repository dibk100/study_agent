from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_experimental.tools import PythonREPLTool

# 파이썬 코드를 실행하는 도구를 생성합니다.
python_tool = PythonREPLTool()

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
print(hf_token)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  # 원하는 허깅페이스 모델
    task="text-generation",
    max_new_tokens=256,
    temperature=0.0,
    huggingfacehub_api_token=hf_token
)

# 파이썬 코드를 실행하고 중간 과정을 출력하고 도구 실행 결과를 반환하는 함수
def print_and_execute(code, debug=True):
    if debug:
        print("CODE:")
        print(code)
    return python_tool.invoke(code)

# 프롬프트
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are Raymond Hetting, an expert python programmer, well versed in meta-programming and elegant, concise and short but well documented code. "
        "Return only the code, no intro, no explanation, no chatty, no markdown, no code block, no nothing. Just the code."
    ),
    ("human", "{input}")
])

# Hugging Face 모델을 LLM으로 연결
chain = prompt | llm | StrOutputParser() | RunnableLambda(print_and_execute)

# 결과 출력
print(chain.invoke("로또 번호 생성기를 출력하는 코드를 작성하세요."))