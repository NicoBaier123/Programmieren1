
import numpy as np
from sympy import symbols, Eq, solve


def parse_vector_input(input_str):
    return [symbols(val.strip()) if val.strip().isalpha() else float(val.strip()) for val in input_str.split(';')]



def gauss_elimination(matrix):
    rows, cols = matrix.shape
    steps = []  # Store the steps of Gaussian elimination

    for i in range(min(rows, cols)):
        pivot_idx = np.argmax(np.abs(matrix[i:, i])) + i
        matrix[[i, pivot_idx]] = matrix[[pivot_idx, i]]

        if matrix[i, i] == 0:
            continue  # Skip if the pivot element is already zero

        step = f"Pivot element: {matrix[i, i]}\n"
        for j in range(i + 1, rows):
            factor = matrix[j, i] / matrix[i, i]
            matrix[j, i:] -= factor * matrix[i, i:]
            step += f"Row {j+1} -= {factor} * Row {i+1}\n"

        steps.append(step)

    return matrix, steps



def check_linear_dependency(vectors):
    matrix = np.array(vectors, dtype=object)  # Use 'object' type to allow for symbolic variables
    augmented_matrix = np.column_stack((matrix, np.eye(len(vectors), dtype=object)))

    reduced_matrix, steps = gauss_elimination(augmented_matrix)

    rank_original = np.linalg.matrix_rank(matrix.astype(float))
    rank_reduced = np.linalg.matrix_rank(reduced_matrix[:, :len(vectors)].astype(float))

    if rank_original == rank_reduced:
        if rank_original == len(vectors):
            return "Die Vektoren sind linear unabhängig."
        else:
            return "Die Vektoren sind linear abhängig. Die Lösungswerte für die Parameter sind frei wählbar."
    else:
        solution_parameters = len(vectors) - rank_reduced

        # Create symbolic parameters directly in the input
        parameters = symbols('x:' + str(solution_parameters))

        # Create equations
        equations = []
        for i in range(rank_reduced, len(vectors)):
            equation = Eq(sum(reduced_matrix[i, j] * parameters[j - rank_reduced] for j in range(rank_reduced, len(vectors))), 0)
            equations.append(equation)

        # Check linear dependence
        is_linear_dependent = any(equation != 0 for equation in equations)

        if is_linear_dependent:
            # Solve the equations
            solution = solve(equations, parameters)

            solution_steps = "\n".join(steps)

            # Save solution steps in a text file
            with open("solution_steps.txt", "w") as file:
                file.write(solution_steps)

            return f"Die Vektoren sind linear abhängig. Die Lösungswerte für die Parameter sind:\n{solution}\n\nLösungsweg wurde in 'solution_steps.txt' gespeichert."

        else:
            return "Die Vektoren sind linear unabhängig."

