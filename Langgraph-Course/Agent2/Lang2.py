from langgraph.graph import StateGraph
from typing import List, TypedDict
import numpy as np

class AgentState(TypedDict):
  nums : List[int]
  name : str
  operation : str
  result : str

  def process_ans(state: AgentState) -> AgentState:
    """Handles the Logic & handles multiple inputs"""

    if state['operation'] == '+':
        state['result'] = f"\nName : {state['name']} \nOperator : {state['operation']} \nResults : {np.sum(state['nums'])}"
    elif state['operation'] == '*':
        state['result'] = f"\nName : {state['name']} \nOperator : {state['operation']} \nResults : {np.prod(state['nums'])}"
    else:
        state['result'] = "\nInvalid Operator"

    return state
