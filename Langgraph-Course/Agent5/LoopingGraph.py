from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from numpy import random


class GameState(TypedDict):
    player_name : str
    target_num : int
    guesses : List[int]
    attempts : int
    lower_bound : int
    upper_bound : int


def set_node(state: GameState) -> GameState:
    state['player_name'] = f"\nHello there {state['player_name']}, Welcome to the Automatic Both Guessing Game."

    state['target_num'] = int(random.randint(1, 20))
    state['guesses'] = []
    state['attempts'] = 0
    state['lower_bound'] = 1
    state['upper_bound'] = 20

    return state


def guessing_game(state: GameState) -> GameState:
    possible_guess = [i for i in range(state['lower_bound'], state['upper_bound']+1) if i not in state['guesses']]

    if possible_guess:
        guess = int(random.choice(possible_guess))
    else:
        guess = int(random.randint(state['lower_bount'], state['upper_bound']))

    state['guesses'].append(guess)
    state['attempts'] += 1

    return state


def check_guess(state: GameState) -> GameState:
    target = state['target_num']
    guess = state['guesses'][-1]

    if guess > target:
        print(f"\nHint : The target number is less than {guess} \nAttempts : {state['attempts']} / 7 \nRange : {state['lower_bound']} - {state['upper_bound']}\n")
        state['upper_bound'] = min(state['upper_bound'], guess - 1)
    
    elif guess < target:
        print(f"\nHint : The target number is greater than {guess} \nAttempts : {state['attempts']} / 7 \nRange : {state['lower_bound']} - {state['upper_bound']}\n")
        state['lower_bound'] = max(state['lower_bound'], guess + 1)

    else:
        print(f"You Guess It. \nAttempts : {state['attempts']} / 7 \nGuessed Number : {guess} \nTarget Number : {target}\n")

    return state


def conditional_edge(state: GameState) -> str:
    guessed_num = state['guesses'][-1]
    target = state['target_num']

    if guessed_num == target:
        return "end"

    elif state['attempts'] == 7:
        print(f"Better luck next time. \nAttempts : {state['attempts']} / 7 \n")
        return "end"

    else:
        return "loop"


graph = StateGraph(GameState)

graph.add_node('set_up_node', set_node)
graph.add_node('guess_node', guessing_game)
graph.add_node('hint_node', check_guess)

graph.add_edge('set_up_node', 'guess_node')
graph.add_edge('guess_node', 'hint_node')
graph.add_conditional_edges(
    'hint_node',
    conditional_edge,
    {
        'end' : END,
        'loop' : 'guess_node'
    }
)

graph.set_entry_point('set_up_node')

app = graph.compile()

result = app.invoke({'player_name' : 'Charise Kimberly'})

print('\n', result['player_name'])