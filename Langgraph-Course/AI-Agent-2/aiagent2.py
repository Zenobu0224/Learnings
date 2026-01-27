from  typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
import os


class AgentState(TypedDict):
    messages : List[Union[BaseMessage, AIMessage]]


# LLM Model
llm = ChatOllama(model="llama3.2:1b")


def process(state: AgentState) -> AgentState:
    response = llm.invoke(state['messages'])

    state['messages'].append(AIMessage(content=response.content))
    print(f"AI : {response.content}\n")

    return state


# Graphing with langgraph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

# Array that store conversation with AI (for memory)
conversation_history = []

if os.path.exists("Langgraph-Course/AI-Agent-2/convo_history.txt"):
    with open("Langgraph-Course/AI-Agent-2/convo_history.txt") as convo_db:
        for msg in convo_db:
            if msg.startswith("You") or msg.startswith("AI"):
                conversation_history.append(msg)

print(f"\n{conversation_history}\n")

user_input = input("Enter Message : ")
while user_input != "bye":
    conversation_history.append(HumanMessage(content=user_input))

    result = agent.invoke({"messages" : conversation_history})

    conversation_history = result["messages"]

    user_input = input("Enter Message : ")


with open("Langgraph-Course/AI-Agent-2/convo_history.txt", "w") as db:
    db.write("\nStart Conversation Logs:\n")

    for msg in conversation_history:
        if isinstance(msg, HumanMessage):
            db.write(f"You : {msg.content}\n")
        elif  isinstance(msg, AIMessage):
            db.write(f"AI : {msg.content}\n\n")
    
    db.write("End Conversation Logs\n")

print("\nSaved to convo_history.txt\n")