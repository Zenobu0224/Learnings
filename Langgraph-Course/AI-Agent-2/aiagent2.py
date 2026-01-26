from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END