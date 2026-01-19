from langgraph.graph import StateGraph, END
from typing import TypedDict, List
import random

class AgentState(TypedDict):
    name : str
    nums : List[int]
    counter : int

def greeter_node(state: AgentState) -> AgentState:
    state['name'] = f"Hello {state['name']}, how's your day?"
    state['counter'] = 0

    return state

def random_node(state: AgentState) -> AgentState:
    state['nums'].append(random.randint(0, 24))
    state['counter'] += 1
    return state


def conditional_node(state: AgentState) -> AgentState:
    if state['counter'] < 7:
        return "loop"
    else:
        return "exit"
    
graph = StateGraph(AgentState)

graph.add_node('greeter_node', greeter_node)
graph.add_node('random_node', random_node)

graph.add_edge('greeter_node', 'random_node')
graph.add_conditional_edges(
    'random_node',
    conditional_node,
    {
        "loop" : "random_node",
        "exit" : END
    }
)

graph.set_entry_point('greeter_node')

app = graph.compile()

results = app.invoke({
    "name" : "Charise Kimberly",
    "nums" : [],
    "counter" : -3
})

print(results)