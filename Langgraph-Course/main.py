from typing import Dict, TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
    msg : str


    