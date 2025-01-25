use pyo3::prelude::*;

/// Generate a Sudoku puzzle grid.
///
/// Creates a valid Sudoku puzzle with the specified difficulty level.
///
/// Args:
///     difficulty (str): The difficulty level of the puzzle.
///         Options are "easy", "medium", and "hard".
///
/// Returns:
///     Vec<Vec<u8>>: A 9x9 grid representing the Sudoku puzzle,
///     where `0` represents an empty cell.
///
/// Example:
///     >>> import puzzle_party
///     >>> sudoku = puzzle_party.generate_sudoku("medium")
///     >>> print(sudoku)
///     [[5, 3, 0, 0, 7, 0, 0, 0, 0], ...]
#[pyfunction]
fn generate_sudoku(_difficulty: &str) -> PyResult<Vec<Vec<u8>>> {
    // Example implementation (stub).
    Ok(vec![vec![0; 9]; 9]) // 9x9 grid of zeros.
}


/// Generate a Nonogram puzzle.
///
/// Creates row and column hints for a Nonogram puzzle.
///
/// Args:
///     width (usize): The width of the puzzle grid.
///     height (usize): The height of the puzzle grid.
///
/// Returns:
///     (Vec<Vec<usize>>, Vec<Vec<usize>>):
///     A tuple containing:
///         - The row clues (list of lists of numbers).
///         - The column clues (list of lists of numbers).
///
/// Example:
///     >>> import puzzle_party
///     >>> row_clues, col_clues = puzzle_party.generate_nonogram(5, 5)
///     >>> print("Row clues:", row_clues)
///     >>> print("Column clues:", col_clues)
///     Row clues: [[1, 3], [2], [5], [1], [2, 2]]
///     Column clues: [[1], [3, 1], [2], [5], [1, 1]]
#[pyfunction]
fn generate_nonogram(_width: usize, _height: usize) -> PyResult<(Vec<Vec<usize>>, Vec<Vec<usize>>)> {
    // Example implementation (stub).
    Ok((vec![vec![1, 3], vec![2], vec![5], vec![1], vec![2, 2]], // Row clues
        vec![vec![1], vec![3, 1], vec![2], vec![5], vec![1, 1]])) // Column clues
}


/// Generate a Minesweeper puzzle.
///
/// Creates a Minesweeper grid with mines randomly placed based on difficulty.
///
/// Args:
///     width (usize): The width of the puzzle grid.
///     height (usize): The height of the puzzle grid.
///     mines (usize): The number of mines to place on the grid.
///
/// Returns:
///     Vec<Vec<u8>>: A 2D grid where:
///         - `0` represents an empty cell,
///         - A number (1-8) represents adjacent mines,
///         - `9` represents a mine.
///
/// Example:
///     >>> import puzzle_party
///     >>> grid = puzzle_party.generate_minesweeper(10, 10, 20)
///     >>> print(grid)
///     [[0, 1, 9, ...], ...]
#[pyfunction]
fn generate_minesweeper(width: usize, height: usize, _mines: usize) -> PyResult<Vec<Vec<u8>>> {
    // Example implementation (stub).
    Ok(vec![vec![0; width]; height])
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn puzzle_party(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(generate_sudoku, m)?)?;
    m.add_function(wrap_pyfunction!(generate_nonogram, m)?)?;
    m.add_function(wrap_pyfunction!(generate_minesweeper, m)?)?;
    Ok(())
}
