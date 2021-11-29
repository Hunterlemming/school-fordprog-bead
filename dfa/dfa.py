from typing import Tuple

from dfa.transitions import Transitions


class DFA:
    initial_state: int = 0
    final_states: Tuple[int] = (8,)

    def start(self) -> None:
        name: str = input("Enter a name to validate!\n")
        valid = self.check(name + "$")
        print("VALID" if valid else "INVALID")

    def check(self, name: str) -> bool:
        current_state = 1
        
        for letter in name:
            transition = Transitions.get(current_state)
            if transition == None: 
                return False
            current_state = transition.get_destination(letter)
        
        return current_state in self.final_states
