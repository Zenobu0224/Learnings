from langgraph.graph import StateGraph
from typing import List, TypedDict
import numpy as np

# --- 1. State Definition ---

class AgentState(TypedDict):
    """
    Represents the internal state of the graph.
    
    Attributes:
        nums: A list of integers to be processed.
        name: The user's name for personalized output.
        operation: The mathematical operator ('+' or '*').
        result: The final formatted string output.
    """
    nums : List[int]
    name : str
    operation : str
    result : str

# --- 2. Node Functions ---

def process_ans(state: AgentState) -> AgentState:
    """
    Node function that performs the mathematical calculation based on state.
    
    Logic:
    - Sums the list if operator is '+'
    - Multiplies the list if operator is '*'
    """
    # Extract values for readability
    op = state['operation']
    numbers = state['nums']
    user_name = state['name']

    if op == '+':
        calc = np.sum(numbers)
        state['result'] = f"\nName : {user_name} \nOperator : {op} \nResults : {calc}"
    elif op == '*':
        calc = np.prod(numbers)
        state['result'] = f"\nName : {user_name} \nOperator : {op} \nResults : {calc}"
    else:
        state['result'] = "\nInvalid Operator"

    return state

# --- 3. Graph Construction ---

# Initialize the graph with our state schema
builder = StateGraph(AgentState)

# Add the processing node
builder.add_node('processing', process_ans)

# Define the flow: Start -> Processing -> End
builder.set_entry_point('processing')
builder.set_finish_point('processing')

# Compile the graph into an executable app
app = builder.compile()

# --- 4. Execution Logic ---

if __name__ == "__main__":
    # Collecting User Inputs
    name = input("Enter Name : ")
    num_length = int(input("Enter length of list : "))
    
    num_list = []
    for i in range(num_length):
        num_val = int(input(f"Enter value {i+1} : "))
        num_list.append(num_val)

    operator = input("Enter Operator (+ or *) : ")

    # Invoke the Graph
    # The dictionary passed here must match the AgentState TypedDict
    initial_input = {
        'nums': num_list, 
        'name': name, 
        'operation': operator
    }
    
    final_state = app.invoke(initial_input)

    # Output the result stored in the state
    print(final_state['result'])