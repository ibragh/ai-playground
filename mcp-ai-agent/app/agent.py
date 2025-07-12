from fastapi import APIRouter
from pydantic import BaseModel
from langchain.agents import AgentExecutor, initialize_agent
from langchain.llms import OpenAI
from langchain.tools import Tool
from .tools.jira_tool import jira_search
from .tools.sql_tool import run_query

class ChatRequest(BaseModel):
    message: str

router = APIRouter()

llm = OpenAI(openai_api_base="http://model:8001/v1")

jira_tool = Tool(
    name="jira",
    func=jira_search,
    description="Interact with Jira"
)

def build_agent():
    return initialize_agent(tools=[jira_tool, Tool(name="sql", func=run_query, description="Run SQL")], llm=llm, agent="chat-zero-shot-react-description")

agent_executor: AgentExecutor = build_agent()

@router.post("/chat")
async def chat(req: ChatRequest):
    response = agent_executor.run(req.message)
    return {"response": response}

agent_router = router
