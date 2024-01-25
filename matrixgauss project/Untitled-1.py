import numpy as np

# Get the size of the matrix from the user
n = int(input("Enter the size of the matrix: "))

# Initialize an empty matrix
A = np.empty((n, n))

# Initialize an empty constants vector
b = np.empty(n)

# Get the elements of the matrix and constants vector from the user
print("Enter the vectors:")
# Check if the linear system of equations is solvable
if np.linalg.det(A) == 0:
    print("The linear system of equations is not solvable.")
else:
    # Solve the linear system of equations
    x = np.linalg.solve(A, b)

    # Print the solution
    print("Solution:")
    print(x)

