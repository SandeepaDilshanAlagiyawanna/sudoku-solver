# Sudoku Solver

This Python project provides a simple yet efficient Sudoku solver using the backtracking algorithm. Sudoku is a popular logic-based number-placement puzzle. The solver can take any 9x9 Sudoku puzzle as input and find a valid solution or determine that no solution exists.

## Features

- Solves standard 9x9 Sudoku puzzles.
- Uses backtracking algorithm to efficiently find solutions.
- Provides clear and user-friendly output of the solved puzzle.
- Handles invalid or unsolvable puzzles gracefully.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/SandeepaDilshanAlagiyawanna/sudoku-solver.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sudoku-solver
    ```

3. Run the Sudoku solver with your input puzzle:

    ```bash
    python sudoku_solver.py
    ```

    Replace `sudoku_solver.py` with the name of your Python script if necessary.

4. Input your Sudoku puzzle in the `sudoku_solver.py` script as a 9x9 grid. Use `0` to represent empty cells, and specify the numbers in the known cells.

5. The solver will either print the solved Sudoku puzzle or indicate that no solution exists.

## Example

```python
# Example Sudoku puzzle as input
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Output (solved Sudoku puzzle):
# [5, 3, 4, 6, 7, 8, 9, 1, 2]
# [6, 7, 2, 1, 9, 5, 3, 4, 8]
# [1, 9, 8, 3, 4, 2, 5, 6, 7]
# [8, 5, 9, 7, 6, 1, 4, 2, 3]
# [4, 2, 6, 8, 5, 3, 7, 9, 1]
# [7, 1, 3, 9, 2, 4, 8, 5, 6]
# [9, 6, 1, 5, 3, 7, 2, 8, 4]
# [2, 8, 7, 4, 1, 9, 6, 3, 5]
# [3, 4, 5, 2, 8, 6, 1, 7, 9]
```

## License

This Sudoku solver is open-source and available under the [MIT License](LICENSE).

Feel free to use, modify, and share it as needed. Contributions are welcome!

