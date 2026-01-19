from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from numpy import random

class AgentState(TypedDict):
  player_name : str
  guesses : List[int]
  target_num : int
  attempts : int
  lower_bound : int
  upper_bound : int


def set_up_node(state: AgentState) -> AgentState:
  state['player_name'] = f"Welcome to the Guessing Game {state['player_name']}!"
  state['guesses'] = []
  state['target_num'] = random.randint(1, 20)
  state['attempts'] = 0
  state['lower_bound'] = 1
  state['upper_bound'] = 20

  return state

def guess_node(state: AgentState) -> AgentState:
  possible_guess = [i for i in range(state['lower_bound'], state['upper_bound']) if i not in state['guesses']]

  if possible_guess:
    guess = random.choice(possible_guess)
  else:
    guess = random.randint(state['lower_bound'], state['upper_bound']+1)

  state['guesses'].append(guess)
  state['attempts'] += 1

  return state


def conditional_edge(state: AgentState) -> AgentState:
  if state['guesses'][-1] == state['target_num']:
    print(f"\nCongrats {state['player_name']} \nYou Guest it Right \nAttempts : {state['attempts']}")
    return "end"
  elif state['attempts'] >= 7:
    print(f"\nBetter luck next time {state['player_name']}. \nYou run out of attempts :(")
    return "end"
  else:
    return "loop"



def hint_node(state: AgentState) -> AgentState:
  latest_guess = state['guesses'][-1]
  target_num = state['target_num']

  if latest_guess > target_num:
    print(f"\nThe guest number is a bit high. \nTry lower number \nAttempts : {state['attempts']}/7")
    state['upper_bound'] = min(state['upper_bound'], latest_guess - 1)

  elif latest_guess < target_num:
    print(f"\nThe guest number is a bit low. \nTry higher number \nAttempts : {state['attempts']}/7")
    state['lower_bound'] = max(state['lower_bound'], latest_guess + 1)

  else:
    print(f"\nYou won\n")

  return state



graph = StateGraph(AgentState)

graph.add_node("set_up_node", set_up_node)
graph.add_node("guess_node", guess_node)
graph.add_node("hint_node", hint_node)

graph.add_edge("set_up_node", "guess_node")
graph.add_edge("guess_node", "hint_node")
graph.add_conditional_edges(
    "hint_node",
    conditional_edge,
    {
        "loop" : "guess_node",
        "end" : END
    }
)

graph.set_entry_point("set_up_node")

app = graph.compile()


result = app.invoke({
    "player_name" : "Charles",
    "guesses" : [],
    "target_num" : 0,
    "attempts" : 0,
    "lower_bound" : 1,
    "upper_bound" : 20
})

print("\n\n", result['target_num'])
print("\n", result['guesses'])
print("\n", result['lower_bound'])
print("\n", result['upper_bound'])