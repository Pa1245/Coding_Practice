import timeit
import math

def main():
    start_time = timeit.default_timer()
    limit = 2000000
    cross_limit = int(math.floor(math.sqrt(limit)))
    sieve = [False] * (limit+1)
    sieve[0] = True
    sieve[1] = True

    for n in range(4, limit+1, 2):
        sieve[n] = True
    for n in range(3, cross_limit, 2):
        if not sieve[n]:
            for m in range(n**2, limit, 2*n):
                sieve[m] = True

    sum_prime = 0
    for n in range(2, limit+1):
        if not sieve[n]:
            sum_prime = sum_prime + n
    print sum_prime
    elapsed = timeit.default_timer() - start_time
    print elapsed

if __name__ == '__main__':
    main()
