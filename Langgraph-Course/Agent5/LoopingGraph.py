from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from numpy import randoms


class GameState(TypedDict):
  player_name : str
  target_num : int
  guesses : List[int]
  attempts : int
  lower_bound : int
  upper_bound : int