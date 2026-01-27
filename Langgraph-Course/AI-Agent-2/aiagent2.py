from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    messages : List[Union[BaseMessage, AIMessage]]


llm = ChatOllama(model="llama3.2:1b")

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state['messages'])

    state['messages'].append(AIMessage(content=response.content))
    print(f"AI : {response.content}\n")

    return state