from typing import TypedDict, List
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START,  END

class AgentState(TypedDict):
    messages : List[BaseMessage]

llm = ChatOllama(model="qwen2.5:3b")

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])

    print(f"AI : {response.content}\n")

    return state

graph = StateGraph(AgentState)

graph.add_node("process", process)

graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

# USER INPUT
user_input = input("\nEnter Message : ")
while user_input != "bye":
    agent.invoke({"messages" : [HumanMessage(content=user_input)]})

    user_input = input("\nEnter Message : ") 