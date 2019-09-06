from typing import List, NamedTuple
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
        self._next_gen: Generation = self._current_gen

    @staticmethod
    def _randomize_generation(rows, cols, liveliness) -> Generation:
        """Creates a randomized generation"""
        generation: Generation = [[Cell.DEAD for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if random.uniform(0, 1.0) < liveliness:
                    generation[r][c] = Cell.ALIVE
        return generation

    def _apply_rules(self) -> None:
        """Applies the rules grid cell by grid cell to update the next generation"""
        # generations are double buffered so that the application of rules doesn't overwrite the current generation
        for r in range(self._rows):
            for c in range(self._cols):
                alive_cells: int = 0
                # for each cell, count the number of alive neighbor cells (8 if statements), don't go out of bounds
                # check North West
                if r - 1 >= 0 and c - 1 >= 0 and self._current_gen[r][c] == Cell.ALIVE:
                    alive_cells += 1

                # check North
                if r - 1 >= 0 and self._current_gen[r][c] == Cell.ALIVE:
                    alive_cells += 1

                # check North East
                if r - 1 >= 0 and c + 1 < self._cols and self._current_gen[r][c] == Cell.ALIVE:
                    alive_cells += 1

                # check East
                if c + 1 < self._cols and self._current_gen[r][c] == Cell.ALIVE:
                    alive_cells += 1

                # check South East
                if r + 1 < self._rows and c + 1 < self._cols and self._current_gen[r][c] == Cell.ALIVE:
                    alive_cells += 1

                # check South
                if r + 1 < self._rows and self._current_gen[r][c] == Cell.ALIVE:
                    alive_cells += 1

                # check South West
                if r + 1 < self._rows and c - 1 >= 0 and self._current_gen[r][c] == Cell.ALIVE:
                    alive_cells += 1

                # check West
                if c - 1 >= 0 and self._current_gen[r][c] == Cell.ALIVE:
                    alive_cells += 1

                # based on the number of alive cells, apply different rules:
                if alive_cells < 2 and self._current_gen[r][c] == Cell.ALIVE:
                    self._next_gen[r][c] = Cell.DEAD  # under population
                elif (alive_cells == 2 or alive_cells == 3) and self._current_gen[r][c] == Cell.ALIVE:
                    self._next_gen[r][c] = Cell.ALIVE  # okay population
                elif alive_cells > 3 and self._current_gen[r][c] == Cell.ALIVE:
                    self._next_gen[r][c] = Cell.DEAD  # over population
                elif alive_cells == 3 and self._current_gen[r][c] == Cell.DEAD:
                    self._next_gen[r][c] = Cell.ALIVE  # reproduction
        self._current_gen = self._next_gen  # update the generation

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
            if verbose:
                print("Season #{}".format(k))
                print(self)
            self._apply_rules()


if __name__ == '__main__':
    random.seed(10)
    game: Game = Game(3, 3, 0.50)
    game.simulate(3)
