from typing import Dict, Tuple
import string


C :str = string.ascii_letters
D :str = string.digits[1:]


class Transition:
    destination_map: Tuple[Tuple[str,int]]

    def __init__(self, c_state: int=0, d_state: int=0, p_state: int=0, u_state: int=0, z_state: int=0, e_state: int=0) -> None:
        """
            Parameters
            ----------
            c_state : int
                Destination state if the input is an upper- or lowercase member of the English alphabet (default is 0).
            d_state : int
                Destination state if the input is a digit in [1, 9] (default is 0).
            p_state : int
                Destination state if the input is '.' (default is 0).
            u_state : int
                Destination state if the input is '_' (default is 0).
            z_state : int
                Destination state if the input is '0' (default is 0).
            e_state : int
                Destination state if the input is '$' (default is 0).
        """
        self.destination_map = (
            (C, c_state),
            (D, d_state),
            (".", p_state),
            ("_", u_state),
            ("0", z_state),
            ("$", e_state)
        )

    def get_destination(self, input: str) -> int:
        for d in self.destination_map:
            if input in d[0]:
                return d[1]
        return 0


Transitions: Dict[int,Transition] = {

    0 : Transition(),

    1 : Transition(p_state=2, u_state=2),

    2 : Transition(d_state=3, z_state=3),

    3 : Transition(d_state=3, c_state=4, u_state=5, z_state=6),

    4 : Transition(c_state=4, u_state=5, d_state=7, z_state=7, e_state=8),

    5 : Transition(e_state=8),

    6 : Transition(u_state=5, c_state=7, d_state=7, p_state=7, e_state=8),

    7 : Transition(u_state=5, c_state=7, d_state=7, z_state=7),

    8 : Transition()

}
