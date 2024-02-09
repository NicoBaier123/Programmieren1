def fibonacci(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n = 100  # Change this to the desired number
fib_sequence = fibonacci(n)
print(fib_sequence)