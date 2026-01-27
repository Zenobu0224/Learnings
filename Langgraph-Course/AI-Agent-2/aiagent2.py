from  typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    messages : List[Union[BaseMessage, AIMessage]]


# LLM Model
llm = ChatOllama(model="llama3.2:1b")

