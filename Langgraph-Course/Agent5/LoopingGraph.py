from langgraph.graph import StateGraph, END
from typing import TypedDict, List
import random

class AgentState(TypedDict):
    name : str
    nums : List[int]
    counter : int