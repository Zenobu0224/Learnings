from typing import Dict, TypedDict
from langgraph.graph import StateGraph


class AgentState(TypedDict):
  msg : str


def greeting_node(state: AgentState) -> AgentState:
  """Simple node that adds a greeting message to the state """

  state['msg'] = 'Hello ' + state['msg'] + ', hows your day?'

  return state


graph = StateGraph(AgentState)

graph.add_node('greeter', greeting_node)

graph.set_entry_point('greeter')
graph.set_finish_point('greeter')

app = graph.compile()

name = input('Enter Name : ')

result = app.invoke({'msg' : name})

print(result['msg'])