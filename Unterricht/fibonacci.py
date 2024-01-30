defaultdict = __import__('collections').defaultdict
count=defaultdict(int)
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    
    count[n] += 1
    
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    
    cache[n] = result
    return result

result = fibonacci(n-1) + fibonacci(n-2)
