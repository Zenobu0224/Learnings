from typing import Dict, TypedDict
from langgraph.graph import StateGraph

# --- 1. STATE DEFINITION ---
# The AgentState defines the "memory" of the graph.
# Every node receives this object and returns an updated version.
class AgentState(TypedDict):
    msg : str


# --- 2. NODE LOGIC ---
# A node is a function where the actual work happens.
def greeting_node(state: AgentState) -> AgentState:
    """Modifies the state by adding a greeting to the 'msg' key."""
    state['msg'] = 'Hello ' + state['msg'] + ', hows your day?'
    return state


# --- 3. GRAPH ORCHESTRATION ---
# Initialize the graph with the state schema.
graph = StateGraph(AgentState)

# Register the node: 'greeter' is the ID, greeting_node is the function.
graph.add_node('greeter', greeting_node)

# Set the flow: Start at 'greeter' and end immediately after.
graph.set_entry_point('greeter')
graph.set_finish_point('greeter')

# Compile the blueprint into a runnable application.
app = graph.compile()


# --- 4. EXECUTION ---
if __name__ == "__main__":
    # Get user input
    name = input('Enter Name : ')

    # Invoke the graph with the initial state
    # result contains the full state after the graph finishes.
    result = app.invoke({'msg' : name})

    # Print the final output
    print(result['msg'])