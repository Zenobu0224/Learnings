from typing import TypedDict, List

class Crush(TypedDict):
    name : str
    year : int

crush_list : List[Crush] = []


for i in range(3):
    name = input('Enter Crush Name : ')
    year = int(input('Enter Year : '))
    print()

    new_crush = Crush(name=name, year=year)

    crush_list.append(new_crush)


print(crush_list)