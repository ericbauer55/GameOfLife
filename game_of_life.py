from typing import List, NamedTuple, TypeVar, Generic
from enum import Enum
import random


class Cell(str, Enum):
    ALIVE = "X"
    DEAD = "."


class CellLocation(NamedTuple):
    row: int
    col: int


# Establish type aliases for CellLocations and grids of locations (a Generation)
Generation = List[List[Cell]]


class Game:
    def __init__(self, rows: int = 10, columns: int = 10, liveliness: float = 0.20) -> None:
        """Create a Game object that stores and evolves generations base on the Game of Life"""
        # setup instance variables
        self._rows: int = rows
        self._cols: int = columns
        self._liveliness: float = liveliness

        # generate random setup
        self._current_gen: Generation = Game._randomize_generation(rows, columns, liveliness)

    @staticmethod
    def _randomize_generation(rows, cols, liveliness) -> Generation:
        """Creates a randomized generation"""
        generation: Generation = [[Cell.DEAD for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if random.uniform(0, 1.0) < liveliness:
                    generation[r][c] = Cell.ALIVE
        return generation

    def __str__(self) -> str:
        """Print the current generation"""
        output: str = ""
        for row in self._current_gen:
            output += "".join([c for c in row])
            output += "\n"
        return output


if __name__ == '__main__':
    game: Game = Game(6, 18, 0.20)
    print(game)
