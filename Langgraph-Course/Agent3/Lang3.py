from langgraph.graph import StateGraph, END
from typing import List, TypedDict

# --- 1. Schema Definition ---

class AgentState(TypedDict):
    """
    The shared memory of the graph.
    Each node can read from and write to these fields.
    """
    name : str
    age : str
    skills : List[str]
    output : str


# --- 2. Node Definitions ---

def node_one(state : AgentState) -> AgentState:
    """Initializes the output string with a greeting."""
    state['output'] = f"Hello {state['name']}, Welcome to the system! "
    return state


def second_node(state: AgentState) -> AgentState:
    """Appends age information to the existing output."""
    state['output'] = state['output'] + f"\nYou are {state['age']} years old!"
    return state


def third_node(state: AgentState) -> AgentState:
    """Appends the list of skills to the final output."""
    # .join() converts the list ['Python', 'AI'] into a string "Python, AI"
    skills_str = ', '.join(state['skills'])
    state['output'] = state['output'] + f"\nYou have skills in: {skills_str}"
    return state

# --- 3. Graph Construction ---

# Define the state machine
builder = StateGraph(AgentState)

# Register the nodes
builder.add_node('first_node', node_one)
builder.add_node('second_node', second_node)
builder.add_node('third_node', third_node)

# Define the flow (Edges)
builder.set_entry_point('first_node')      # Start here
builder.add_edge('first_node', 'second_node') # Move from node 1 to 2
builder.add_edge('second_node', 'third_node') # Move from node 2 to 3
builder.add_edge('third_node', END)          # Finish after node 3

# Compile into an executable application
app = builder.compile()

# --- 4. Main Execution ---

if __name__ == "__main__":
    # Gather user data
    user_name = input("Enter Name : ")
    user_age = input("Enter Age : ")
    num_of_skills = int(input("How many skills do you have? : "))

    skill_list = [input(f"Enter Skill {i+1} : ") for i in range(num_of_skills)]

    # Run the graph
    # We provide the initial state; 'output' starts empty
    results = app.invoke({
        'name': user_name,
        'age': user_age,
        'skills': skill_list
    })

    print('\n\n--- Results ---')
    print(results['output'])

    # Printing the full state shows how all keys were preserved
    print('\nFull State Object:', results)