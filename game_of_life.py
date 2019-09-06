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
        generation: Generation = [[Cell.DEAD for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if random.uniform(0, 1.0) < liveliness:
                    generation[r][c] = Cell.ALIVE
        return generation

    @staticmethod
    def _apply_rules(generation: Generation) -> Generation:
        """Applies the rules grid cell by grid cell to update the next generation"""
        # generations are double buffered so that the application of rules doesn't overwrite the current generation
        return generation

    def __str__(self) -> str:
        """Print the current generation"""
        output: str = ""
        for row in self._current_gen:
            output += "".join([c for c in row])
            output += "\n"
        return output

    def simulate(self, n_seasons: int, verbose: bool = True):
        """Simulates the Rules of the Game of Life for n number of seasons"""
        for k in range(n_seasons):
            self._current_gen = self._apply_rules(self._current_gen)
            if verbose:
                print("Season #{}".format(k))
                print(self)


if __name__ == '__main__':
    game: Game = Game(6, 18, 0.20)
    game.simulate(10)
