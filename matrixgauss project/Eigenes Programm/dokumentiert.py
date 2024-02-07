import numpy as np
from sympy import symbols, Eq, solve


def parse_vector_input(input_str):
    return [symbols(val.strip()) if val.strip().isalpha() else float(val.strip()) for val in input_str.split(';')]


def gauss_elimination(matrix):
    rows, cols = matrix.shape # matrix.shape returns a tuple with the number of rows and columns
    steps = []  # Store the steps of Gaussian elimination

    for i in range(min(rows, cols)): # Iterate over the minimum of the number of rows and columns
        pivot_idx = np.argmax(np.abs(matrix[i:, i])) + i # Find the index of the maximum absolute value in the column
        matrix[[i, pivot_idx]] = matrix[[pivot_idx, i]] # Swap the rows to move the pivot element to the diagonal

        if matrix[i, i] == 0: # Skip if the pivot element is already zero
            continue  # Skip if the pivot element is already zero

        step = f"Pivot element: {matrix[i, i]}\n" # Store the pivot element
        for j in range(i + 1, rows): # Iterate over the rows below the pivot element
            factor = matrix[j, i] / matrix[i, i] # Calculate the factor to eliminate the element below the pivot element
            matrix[j, i:] -= factor * matrix[i, i:] # Eliminate the element below the pivot element
            step += f"Row {j+1} -= {factor} * Row {i+1}\n" # Store the step

        steps.append(step) # Store the step

    return matrix, steps # Return the reduced matrix and the steps of Gaussian elimination

#######Ab hier weiter debuggen########

def check_linear_dependency(vectors): # Check the linear dependency of a list of vectors
    matrix = np.array(vectors, dtype=object)  # Use 'object' type to allow for symbolic variables
    augmented_matrix = np.column_stack((matrix, np.eye(len(vectors), dtype=object))) 

    reduced_matrix, steps = gauss_elimination(augmented_matrix)

    rank_reduced = np.linalg.matrix_rank(reduced_matrix[:, :len(vectors)].astype(float))

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

    with open("solution_steps.txt", "w") as file:
        if is_linear_dependent:
            # Linear dependent case
            file.write("Die Vektoren sind linear abhängig.\n\n")
            file.write("Lösungsweg:\n")
            file.write("Gaußsche Eliminationsschritte:\n")
            for step in steps:
                file.write(step)
                file.write("\n")
            file.write("\n")
            file.write("Lineare Gleichungssysteme:\n")
            for i, eq in enumerate(equations):
                file.write(f"Schritt {i+1}: {eq}\n")

            if solution_parameters > 0:
                # Solve the equations
                solution = solve(equations, parameters)[0]  # Get the first solution from the list
                file.write("\nLösungswerte für die Parameter:\n")
                for param, val in solution.items():
                    file.write(f"{param}: {val}\n")
        else:
            # Linear independent case
            file.write("Die Vektoren sind linear unabhängig.\n\n")
            file.write("Lösungsweg:\n")
            file.write("Gaußsche Eliminationsschritte:\n")
            for step in steps:
                file.write(step)
                file.write("\n")

    if is_linear_dependent:
        if solution_parameters > 0:
            return f"Die Vektoren sind linear abhängig. Die Lösungswerte für die Parameter sind:\n{solution}\n\nLösungsweg wurde in 'solution_steps.txt' gespeichert."
        else:
            return "Die Vektoren sind linear abhängig. Die Lösungswerte für die Parameter sind frei wählbar."
    else:
        return "Die Vektoren sind linear unabhängig."


def main():
    num_vectors = int(input("Bitte geben Sie die Anzahl der Vektoren ein: "))
    vectors = []
    for i in range(num_vectors):
        print(f"Bitte geben Sie die Werte für Vektor {i+1} im Format 'x;y;z' ein:")
        vector_input = input()
        vectors.append(parse_vector_input(vector_input))

    result = check_linear_dependency(vectors)
    print(result)


if __name__ == "__main__":
    main()
