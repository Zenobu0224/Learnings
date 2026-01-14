from typing import Union

def square(x: Union[int, float]) -> float:
    return x * x

x = 5

squared = square(x)

print(squared)