from typing import TypedDict, List
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START,  END

class AgentState(TypedDict):
    messages : List[BaseMessage]

llm = ChatOllama(model="llama3.2:1b")