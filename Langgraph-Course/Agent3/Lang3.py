from langgraph.graph import StateGraph, END
from typing import List, TypedDict

class AgentState(TypedDict):
  name : str
  year : str
  course : str
  final : str