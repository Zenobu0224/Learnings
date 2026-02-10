from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
import os


class AgentState(TypedDict):
    messages : List[BaseMessage]

# LLM Model
llm = ChatOllama(model="qwen2.5:3b")

def processing(state: AgentState) -> AgentState:
    """Processing Node"""
    response = llm.invoke(state["messages"])

    state["messages"].append(AIMessage(content=response.content))

    return state