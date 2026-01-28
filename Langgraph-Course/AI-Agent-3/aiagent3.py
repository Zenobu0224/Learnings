from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.graph.message import add_message
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode


class AgentState(TypedDict):
    messages : Annotated[Sequence[BaseMessage], add_message]


@tool
def add(a : int, b: int):
    """This is an addition function that adds 2 numbers together"""

    return a+b

tools = [add]

llm = ChatOllama(model="llama3.2:1b")


def model_call(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(
        content = "You are a helpful assistant. Use tools for any math."
    )

    response = llm.invoke([system_prompt] + list(state['messages']))

    return {"messages" : response}


def should_continue(state: AgentState) -> str:
    messages = state['messages']
    last_msg = messages[-1]

    if not last_msg.tool_calls:
        return "end"
    else:
        return "use_tool"
    

graph = StateGraph(AgentState)
graph.add_node("agent", model_call)

tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("agent")
graph.add_conditional_edges(
    "agent",
    should_continue,
    {
        "end" : END,
        "use_tool" : "tools"
    }
)

graph.add_edge("tools", "agent")

model = graph.compile()