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
    print(f"AI : {response.content}")

    return state

graph = StateGraph(AgentState)
graph.add_node("model", processing)
graph.set_entry_point("model")
graph.add_edge("model", END)

agent = graph.compile()

# stores conversation history (list)
conversation_hist = []

# checks if convo-db (txt-file) exists
if os.path.exists("Langgraph-Course/AI-Agent-2/convo-history.txt"):

    # opens convo-db (txt-file) and appends every convo(Human & AI) to the conversation_hist list
    with open("Langgraph-Course/AI-Agent-2/convo-history.txt") as txt_file:
        for convo in txt_file:
            if convo.startswith("You") or convo.startswith("AI"):
                conversation_hist.append(convo)

while True:
    msg = input("\n\nYou : ")

    if msg.lower() in ['bye', 'exit']:
        print("\nAI : Sayonara~")
        break

    conversation_hist.append(HumanMessage(content=msg))

    result = agent.invoke({"messages" : conversation_hist})

    conversation_hist = result["messages"]