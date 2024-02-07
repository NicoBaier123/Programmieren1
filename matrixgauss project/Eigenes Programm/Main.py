import numpy as np
from sympy import symbols, Eq, solve
import MatrixCalc as MC


# User input for vectors with variables
def main():
    
    num_vectors = int(input("Bitte geben Sie die Anzahl der Vektoren ein: "))
    vectors = []
    for i in range(num_vectors):
        print(f"Bitte geben Sie die Werte für Vektor {i+1} im Format 'x;y;z' ein:")
        vector_input = input()
        vectors.append(MC.parse_vector_input(vector_input))

    result = MC.check_linear_dependency(vectors)
    print(result)


if __name__ == "__main__":
    main()

    