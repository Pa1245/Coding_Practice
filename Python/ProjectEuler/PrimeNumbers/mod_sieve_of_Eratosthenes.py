# Description: Not considering even numbers in sieving to reduce usage of memory.

import math
import timeit

def main():
    start_time = timeit.default_timer()

    limit = 2000000
    sieve_bound = (limit-1)//2
    sieve = [False]*(sieve_bound+1)
    #print len(sieve)
    sieve[0] = True

    cross_limit = int((math.floor(math.sqrt(limit))-1)/2)
    for i in range(1, cross_limit+1):
        if not sieve[i]:
            for j in range(2*i*(i+1), sieve_bound+1, (2*i)+1):
                sieve[j] = True
    sum_prime = 2
    #print sieve[:11]

    for i in range(1, sieve_bound+1):
        if not sieve[i]:
            sum_prime = sum_prime + (2*i+1)

    elapsed = timeit.default_timer() - start_time

    print sum_prime
    print sum_prime-142913828922
    print elapsed

if __name__ == '__main__':
    main()
