import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logging.debug("This is a debug message")
logging.error("This is an error message")

def fibonacci(n):
    logging.info(f"Calculating fibonacci({n})")
    if n <= 1:
        return n
    else:
        logging.info(f"Calculating fibonacci({n-1}) + fibonacci({n-2})")
        return fibonacci(n-1) + fibonacci(n-2)

def test_fibonacci():
    logging.info("Testing fibonacci function")
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765

test_fibonacci()
print(fibonacci(20))