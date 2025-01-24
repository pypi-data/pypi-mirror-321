from typing import List, Optional
from pysat.solvers import Solver
from pysat.formula import CNF
from .utils.sudoku_error import SudokuError


class DPLLSolver:
    """DPLL-based Sudoku solver using SAT encoding.

    Solves 25x25 Sudoku puzzles by converting them to CNF (Conjunctive Normal Form)
    and using DPLL to find a satisfying assignment.

    Attributes:
        sudoku (List[List[int]]): Input puzzle as 25x25 grid
        size (int): Grid size (25)
        cnf (CNF): PySAT CNF formula object
        solver (Solver): PySAT Glucose3 solver instance
        propagated_clauses (int): Counter for clause additions

    Example:
        >>> puzzle = [[0 for _ in range(25)] for _ in range(25)]
        >>> solver = DPLLSolver(puzzle)
        >>> solution = solver.solve()
    """

    def __init__(self, sudoku: List[List[int]]) -> None:
        """Initialize DPLL Sudoku solver.

        Args:
            sudoku: 25x25 grid with values 0-25 (0 for empty cells)

        Raises:
            SudokuError: If puzzle format is invalid
        """
        if not sudoku or not isinstance(sudoku, list) or len(sudoku) != 25:
            raise SudokuError("Invalid Sudoku puzzle: must be a 25x25 grid")

        self.sudoku = sudoku
        self.size = 25
        self.cnf = CNF()  # CNF object to store Boolean clauses
        self.solver = Solver(name="glucose3")  # Low-level SAT solver
        self.propagated_clauses = 0  # Add clause counter

    def _count_clause(self) -> None:
        self.propagated_clauses += 1

    def add_sudoku_clauses(self) -> None:
        size = self.size
        block_size = int(size**0.5)

        def get_var(row, col, num):
            return row * size * size + col * size + num

        # At least one number in each cell
        for row in range(size):
            for col in range(size):
                self.cnf.append([get_var(row, col, num) for num in range(1, size + 1)])
                self._count_clause()

                # At most one number in each cell
                for num1 in range(1, size + 1):
                    for num2 in range(num1 + 1, size + 1):
                        self.cnf.append(
                            [-get_var(row, col, num1), -get_var(row, col, num2)]
                        )
                        self._count_clause()

        # Add row constraints
        for row in range(size):
            for num in range(1, size + 1):
                self.cnf.append([get_var(row, col, num) for col in range(size)])
                self._count_clause()

        # Add column constraints
        for col in range(size):
            for num in range(1, size + 1):
                self.cnf.append([get_var(row, col, num) for row in range(size)])
                self._count_clause()

        # Add block constraints
        for block_row in range(block_size):
            for block_col in range(block_size):
                for num in range(1, size + 1):
                    self.cnf.append(
                        [
                            get_var(
                                block_row * block_size + i,
                                block_col * block_size + j,
                                num,
                            )
                            for i in range(block_size)
                            for j in range(block_size)
                        ]
                    )
                    self._count_clause()

        # Add initial assignments from the puzzle
        for row in range(size):
            for col in range(size):
                if self.sudoku[row][col] != 0:
                    num = self.sudoku[row][col]
                    self.cnf.append([get_var(row, col, num)])
                    self._count_clause()

    def extract_solution(self, model: List[int]) -> List[List[int]]:
        solution = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for var in model:
            if var > 0:  # Only consider positive assignments
                var -= 1
                num = var % self.size + 1
                col = (var // self.size) % self.size
                row = var // (self.size * self.size)
                solution[row][col] = num
        return solution

    def validate_solution(self, solution: List[List[int]]) -> bool:
        size = self.size
        block_size = int(size**0.5)

        # Validate rows
        for row in solution:
            if len(set(row)) != size or not all(1 <= num <= size for num in row):
                return False

        # Validate columns
        for col in range(size):
            column = [solution[row][col] for row in range(size)]
            if len(set(column)) != size:
                return False

        # Validate blocks
        for block_row in range(block_size):
            for block_col in range(block_size):
                block = [
                    solution[block_row * block_size + i][block_col * block_size + j]
                    for i in range(block_size)
                    for j in range(block_size)
                ]
                if len(set(block)) != size:
                    return False

        return True

    def solve(self) -> Optional[List[List[int]]]:
        """Solve Sudoku puzzle using DPLL SAT solver.

        Returns:
            Solved 25x25 grid if satisfiable, None if unsatisfiable

        Raises:
            SudokuError: If solver produces invalid solution
            Exception: For other solver errors

        Note:
            Uses Glucose3 SAT solver from PySAT
        """
        self.add_sudoku_clauses()
        self.solver.append_formula(self.cnf.clauses)

        try:
            if self.solver.solve():
                # Extract and validate the solution
                model = self.solver.get_model()
                solution = self.extract_solution(model)

                if self.validate_solution(solution):
                    return solution
                else:
                    raise SudokuError("Invalid solution generated.")
            else:
                # If unsat, return None
                return None

        except Exception as e:
            raise
