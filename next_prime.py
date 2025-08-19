#returns a generator that will yield an unlimited number of primes, starting from the first prime (2).
import math

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # Optimization: Exclude even numbers (except 2)
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):  # Iterate only over odd divisors
        if n % i == 0:
            return False
    return True

def next_prime():
    """Returns a generator that will yield an unlimited number of primes."""
    yield 2  # The first prime number
    num = 3   # Start checking from the next odd number
    while True:
        if is_prime(num):
            yield num
        num += 2 # Check only odd numbers for primality






primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]