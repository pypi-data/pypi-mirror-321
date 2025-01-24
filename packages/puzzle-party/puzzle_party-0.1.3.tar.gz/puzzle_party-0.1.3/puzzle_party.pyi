"""
Stub file for the `puzzle_party` module, implemented in Rust.

This file defines the functions and types available in the module for better
intellisense and type checking support in Python.
"""

from typing import List, Tuple

def generate_sudoku(difficulty: str) -> List[List[int]]:
    """
    Generate a Sudoku puzzle grid.

    Creates a valid Sudoku puzzle with the specified difficulty level.

    Args:
        difficulty (str): The difficulty level of the puzzle.
            Options are "easy", "medium", and "hard".

    Returns:
        List[List[int]]: A 9x9 grid representing the Sudoku puzzle,
        where `0` represents an empty cell.

    Example:
        >>> import puzzle_party
        >>> sudoku = puzzle_party.generate_sudoku("medium")
        >>> print(sudoku)
        [[5, 3, 0, 0, 7, 0, 0, 0, 0], ...]
    """
    ...

def generate_nonogram(width: int, height: int) -> Tuple[List[List[int]], List[List[int]]]:
    """
    Generate a Nonogram puzzle.

    Creates row and column hints for a Nonogram puzzle.

    Args:
        width (int): The width of the puzzle grid.
        height (int): The height of the puzzle grid.

    Returns:
        Tuple[List[List[int]], List[List[int]]]:
        A tuple containing:
            - The row clues (list of lists of numbers).
            - The column clues (list of lists of numbers).

    Example:
        >>> import puzzle_party
        >>> row_clues, col_clues = puzzle_party.generate_nonogram(5, 5)
        >>> print("Row clues:", row_clues)
        >>> print("Column clues:", col_clues)
        Row clues: [[1, 3], [2], [5], [1], [2, 2]]
        Column clues: [[1], [3, 1], [2], [5], [1, 1]]
    """
    ...

def generate_minesweeper(width: int, height: int, mines: int) -> List[List[int]]:
    """
    Generate a Minesweeper puzzle.

    Creates a Minesweeper grid with mines randomly placed based on difficulty.

    Args:
        width (int): The width of the puzzle grid.
        height (int): The height of the puzzle grid.
        mines (int): The number of mines to place on the grid.

    Returns:
        List[List[int]]: A 2D grid where:
            - `0` represents an empty cell,
            - A number (1-8) represents adjacent mines,
            - `9` represents a mine.

    Example:
        >>> import puzzle_party
        >>> grid = puzzle_party.generate_minesweeper(10, 10, 20)
        >>> print(grid)
        [[0, 1, 9, ...], ...]
    """
    ...
