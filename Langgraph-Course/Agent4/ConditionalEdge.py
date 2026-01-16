from langgraph.graph import StateGraph, START, END
from typing import TypedDict
import numpy as np

class AgentState(TypedDict):
    num1 : int
    operation1 : str
    num2 : int

    num3 : int
    operation2 : str
    num4 : int

    result1 : str
    result2 : str


def add_node1(state: AgentState) -> AgentState:
    state["result1"] = f"{state['num1']} + {state['num2']} = {state['num1'] + state['num2']}"

    return state

def sub_node1(state: AgentState) -> AgentState:
    state["result1"] = f"{state['num1']} - {state['num2']} = {state['num1'] - state['num2']}"

    return state

def conditional_edge1(state: AgentState) -> AgentState:
    if state["operation1"] == "+":
        return "add_edge1"
    elif state["operation1"] == "-":
        return "sub_edge1"

def add_node2(state: AgentState) -> AgentState:
    state["result2"] = f"{state['num3']} + {state['num4']} = {state['num3'] + state['num4']}"
    
    return state


def sub_node2(state: AgentState) -> AgentState:
    state["result2"] = f"{state['num3']} - {state['num4']} = {state['num3'] - state['num4']}"

    return state


def conditional_edge2(state: AgentState) -> AgentState:
    if state["operation2"] == "+":
        return "add_edge2"
    elif state["operation2"] == "-":
        return "sub_edge2"

graph = StateGraph(AgentState)

graph.add_node("add_node1", add_node1)
graph.add_node("sub_node1", sub_node1)
graph.add_node("router1", lambda state: state)

graph.add_node("add_node2", add_node2)
graph.add_node("sub_node2", sub_node2)
graph.add_node("router2", lambda state: state)

graph.add_edge(START, "router1")
graph.add_conditional_edges(
    "router1",
    conditional_edge1,
    {
        "add_edge1" : "add_node1",
        "sub_edge1" : "sub_node1"
    }
)
graph.add_edge("add_node1", "router2")
graph.add_edge("sub_node1", "router2")
graph.add_conditional_edges(
    "router2",
    conditional_edge2,
    {
        "add_edge2" : "add_node2",
        "sub_edge2" : "sub_node2"
    }
)
graph.add_edge("add_node2", END)
graph.add_edge("sub_node2", END)

app = graph.compile()

result = app.invoke({
    "num1" : 10,
    "operation1" : "-",
    "num2" : 5,

    "num3" : 7,
    "operation2" : "+",
    "num4" : 2
})

print(result['result1'])
print(result['result2'])