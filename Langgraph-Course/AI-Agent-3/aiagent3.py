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