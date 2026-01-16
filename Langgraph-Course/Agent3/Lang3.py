from langgraph.graph import StateGraph, END
from typing import List, TypedDict

class AgentState(TypedDict):
  name : str
  age : str
  skills : List[str]
  output : str
  

def node_one(state : AgentState) -> AgentState:
    """First node that process the name"""

    state['output'] = f"Hello {state['name']}, Welcome to the system! "

    return state


def second_node(state: AgentState) -> AgentState:
    """Second node that process the age"""

    state['output'] = state['output'] + f'\nYou are {state['age']} years old! '

    return state


def third_node(state: AgentState) -> AgentState:
    """Third node that process the skills"""

    state['output'] = state['output'] + f'\nYou have skiils in: {', '.join(state['skills'])}'

    return state
