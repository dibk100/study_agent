# study_agent
Learning and experimenting with AI agents.
- reference : [랭체인LangChain노트](https://wikidocs.net/233782)   
   
## 📋 Agent 구성요소(LangChain)
- Agent: 의사 결정을 담당하는 핵심 컴포넌트.
- Tools: 에이전트가 사용할 수 있는 기능들의 집합.
- Toolkits: 관련된 도구들의 그룹.
- AgentExecutor: 에이전트의 실행을 관리하는 컴포넌트.

## ⚙️ 작동 방식
```
[1] 입력 수신 : 사용자로부터 작업/질문 수신  
    ↓  
[2] 계획 수립 : 단계별 실행 계획 수립  
    ↓  
[3] 도구 선택 : 각 단계에 적합한 도구 선택  
    ↓  
[4] 실행 : 선택한 도구를 사용하여 작업 수행  
    ↓  
[5] 결과 평가 : 결과 검토 및 필요 시 계획 조정  
    ↓  
[6] 출력 생성 : 최종 결과/답변 사용자에게 제공
```