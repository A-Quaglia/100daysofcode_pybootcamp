import csv
from dataclasses import dataclass
from typing import List

@dataclass
class StateCoord:
    name: str
    coor_x: int
    coor_y: int

    def __post_init__(self):
        try:
            self.coor_x = int(self.coor_x)
            self.coor_y = int(self.coor_y)
        except ValueError:
            if self.coor_x == 'x' and self.coor_y =='y':
                pass

class StatesQuiz:
    def __init__(self, states_coords) -> None:
        self.states: List[StateCoord] =  self._read_states_coords_file(states_coords)

    def _read_states_coords_file(self, states_coords):
        with open(states_coords) as data_file:
            data = csv.reader(data_file)
            ls_states = list()
            for entry in data:
                ls_states.append(StateCoord(*entry))

        return ls_states[1:]
    
    def search_state(self, state: str) -> StateCoord:
        state = list(filter(lambda x: x.name==state, self.states))
        if state:
            return state[0]
        else: return None

if __name__ == "__main__":
    states = StatesQuiz("50_states.csv")