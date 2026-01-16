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