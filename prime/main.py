
from sys import exit        # for main
from math import pow, sqrt  # For main 

from time import time       # For timeit
# For profile_memory
import functools
import os
import psutil


def timeit(f):
    def timed(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print ("func:%r args:[%r, %r] took: %2.4f sec" % (f.__name__, args, kw, te-ts))
        return result
    return timed

def profile_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss / 1024 ** 2  # in MB
        result = func(*args, **kwargs)
        mem_after = process.memory_info().rss / 1024 ** 2  # in MB
        print(f"Function {func.__name__} memory usage: {mem_after - mem_before:.4f} MB")
        return result
    return wrapper


@timeit
@profile_memory
def sieve_of_eratosthenes(n)->list:
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

@timeit
@profile_memory
def sieve_of_eratosthenes_sqrt(n)->list:
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    sqrt_n = int(n ** 0.5) + 1
    for i in range(2, sqrt_n):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    # Add remaining primes beyond sqrt_n
    for i in range(sqrt_n, n + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


@timeit
@profile_memory
def sieve_of_eratosthenes_new(limit)->list:
    """
    Generates all prime numbers up to a given limit using the Sieve of Eratosthenes.
    Returns a list of prime numbers.
    """
    if limit <= 1:
        return []

    primes = [True] * (limit + 1)  # Initialize all numbers as potentially prime.
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers.

    # Iterate from 2 up to the square root of the limit.
    for p in range(2, int(sqrt(limit)) + 1):
        if primes[p]:  # If p is prime.
            # Mark all multiples of p as composite (not prime), starting from p*p.
            for multiple in range(p * p, limit + 1, p):
                primes[multiple] = False

    # Collect the prime numbers.
    result = [i for i in range(limit + 1) if primes[i]]
    return result


import random

def _is_composite(n, a, d, s)->bool:
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return False
    return True

def miller_rabin(n, k=5)->bool:  # k is the number of rounds for accuracy.
    """
    Performs the Miller-Rabin primality test.
    Returns True if n is probably prime, False if n is composite.
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1  # Equivalent to d = d // 2
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        if _is_composite(n, a, d, s):
            return False
    return True


def main():
    power = 31
    n = int(pow(2, power) - 1) 
    print(n)
    primes = sieve_of_eratosthenes_new(n)
    print(f"The number of primes in 2^{power}={n} is {len(primes)}")
    print(primes[0])
    

if __name__ == "__main__":   
    exit(main())
    
