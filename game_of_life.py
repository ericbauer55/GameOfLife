from typing import List, NamedTuple
from enum import Enum
import random
import copy


class Cell(str, Enum):
    ALIVE = "X"
    DEAD = "."


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
        # this next line will assign next_gen to point to the same object as current_gen
        # you can check this by saying: g = Game(); g._current_gen is g._next_gen # True
        # https://www.youtube.com/watch?v=mO_dS3rXDIs
        # self._next_gen: Generation = self._current_gen
        # This next way only creates a shallow copy, meaning the list of list is now a list of references
        # self._next_gen: Generation = copy.copy(self._current_gen)
        # self._next_gen: Generation = self._current_gen.copy()  # shallow copy
        # This final way is the way to truly copy every element
        self._next_gen: Generation = copy.deepcopy(self._current_gen)

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
                if r - 1 >= 0 and c - 1 >= 0 and self._current_gen[r - 1][c - 1] == Cell.ALIVE:
                    alive_cells += 1

                # check North
                if r - 1 >= 0 and self._current_gen[r - 1][c] == Cell.ALIVE:
                    alive_cells += 1

                # check North East
                if r - 1 >= 0 and c + 1 < self._cols and self._current_gen[r - 1][c + 1] == Cell.ALIVE:
                    alive_cells += 1

                # check East
                if c + 1 < self._cols and self._current_gen[r][c + 1] == Cell.ALIVE:
                    alive_cells += 1

                # check South East
                if r + 1 < self._rows and c + 1 < self._cols and self._current_gen[r + 1][c + 1] == Cell.ALIVE:
                    alive_cells += 1

                # check South
                if r + 1 < self._rows and self._current_gen[r + 1][c] == Cell.ALIVE:
                    alive_cells += 1

                # check South West
                if r + 1 < self._rows and c - 1 >= 0 and self._current_gen[r + 1][c -1] == Cell.ALIVE:
                    alive_cells += 1

                # check West
                if c - 1 >= 0 and self._current_gen[r][c - 1] == Cell.ALIVE:
                    alive_cells += 1

                # based on the number of alive cells, apply different rules:
                self._next_gen[r][c] = Game.check_ruleset(alive_cells, self._current_gen[r][c])

        self._current_gen = copy.deepcopy(self._next_gen)  # update the generation

    @staticmethod
    def check_ruleset(number_alive: int, current_state: Cell) -> Cell:
        """Determines if a cell is alive next generation given its current state and alive neighbors"""
        if number_alive < 0:
            raise (ValueError('Value of number_alive cannot be negative'))
        if current_state == Cell.ALIVE:
            if number_alive < 2:
                return Cell.DEAD
            elif number_alive == 2 or number_alive == 3:
                return Cell.ALIVE
            elif number_alive > 3:
                return Cell.DEAD
        else:
            if number_alive == 3:
                return Cell.ALIVE
            else:
                return Cell.DEAD

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
    game: Game = Game(6, 30, 0.20)
    game.simulate(20)
