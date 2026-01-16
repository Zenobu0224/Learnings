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
