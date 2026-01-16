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

graph = StateGraph(AgentState)

graph.add_node('first_node', node_one)
graph.add_node('second_node', second_node)
graph.add_node('third_node', third_node)

graph.set_entry_point('first_node')
graph.add_edge('first_node', 'second_node')
graph.add_edge('second_node', 'third_node')
graph.add_edge('third_node', END)

app = graph.compile()


skill_list = []

name = input("Enter Name : ")
age = input("Enter Age : ")

num_of_skills = int(input("How many skills do you have? : "))

for i in range(num_of_skills):
  skill = input(f"Enter Skill {i+1} : ")
  skill_list.append(skill)

results = app.invoke({'name' : name,
                      'age' : age,
                      'skills' : skill_list})

print('\n\nResults:\n')
print(results['output'])

print('\n', results)
