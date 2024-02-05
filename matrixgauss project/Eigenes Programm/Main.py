import numpy as np
from sympy import symbols, Eq, solve
import MatrixCalc as MC


# User input for vectors with variables
def main():
    vectors = []
    num_vectors = int(input("Enter the number of vectors: "))
    for i in range(num_vectors):
        vector_input = input(f"Enter vector {i+1} as semi-colon-separated values (e.g., 1; x; 2): ")
        vector = MC.parse_vector_input(vector_input)
        vectors.append(vector)

    result = MC.check_linear_dependency(vectors)
    print(result)


if __name__ == '__main__':
    main()