from pydantic import BaseModel
from typing import Annotated, List, Generator
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, AIMessageChunk
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from scout.tools import query_db, generate_visualization
from scout.prompts import prompts


class  ScoutState(BaseModel):
    messages: Annotated[List[BaseMessage], add_messages] = []
    chart_json: str = ""




llm= ChatOpenAI(name= "Scout", model="gpt-4.1-mini-2025-04-14")

llm.invoke('hi')


def assistant_node(state:ScoutState) -> ScoutState:
    response= llm.invoke('hi Scount')
    state.messages.append(response)

    return state

state = ScoutState(
    messages=[HumanMessage(content='hi')],
    chart_json="this is the chart json",
)

result = assistant_node(state)

print(result.model_dump_json(indent=2))