from typing import Optional

def message(msg : Optional[str]) -> None:
    if msg is None:
        print('Eden Pearl')
    else:
        print(f'{msg} <3')

message(msg="Devine Lorraine mahal parin kita kahit maldita ka!!")