import numpy as np

def vectors_to_matrix(vectors):
    matrix = np.array(vectors).T
    return matrix

# Benutzereingabe Anzahl Vektoren
vectors = []
num_vectors = int(input("Enter the number of vectors: "))
for i in range(num_vectors):
    vector = input(f"Enter vector {i+1}: ").split()
    vectors.append(vector)

matrix = vectors_to_matrix(vectors)
print(matrix)