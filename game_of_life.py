from typing import List, NamedTuple, TypeVar, Generic
import enum
import random


class Cell(enum):
    ALIVE = "X"
    DEAD = "."


class CellLocation(NamedTuple):
    row: int
    col: int
    state: Cell


# Establish type aliases for CellLocations and grids of locations (a Generation)
Generation = List[List[CellLocation]]


class Game:
    def __init__(self, rows: int = 10, columns: int = 10, liveliness: float = 0.20) -> None:
        """Create a Game object that stores and evolves generations base on the Game of Life"""
        # setup instance variables
        self._rows: int = rows
        self._cols: int = columns
        self._liveliness: float = liveliness

        # generate random setup
        self._current_gen: Generation = self._randomize_generation(rows, columns, liveliness)

    @staticmethod
    def _randomize_generation(self, rows, cols, liveliness) -> Generation:
        """Creates a randomized generation"""
        generation: Generation = [[c.state.join(Cell.DEAD) for c in cols] for r in rows]
        for r in rows:
            for c in cols:
                if random.uniform(0, 1.0) < liveliness:
                    generation[r][c].state = Cell.ALIVE
        return generation

    def __str__(self) -> str:
        """Print the current generation"""
        output: str = ""
        for row in self._current_gen:
            output += ["".join(c.state for c in row)]
            output += "\n"
        return output


if __name__ == '__main__':
    game: Game = Game()
    print(game)
