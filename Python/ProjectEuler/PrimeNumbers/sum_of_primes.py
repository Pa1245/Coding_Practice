import math
import timeit

def isPrime(number):
    if number == 1:
        return False
    elif number<4:
        return True
    elif number%2 == 0:
        return False
    elif number < 9:
        return True
    elif number%3 == 0:
        return False
    else:
        limit = math.sqrt(number)
        i = 5
        while i <= limit:
            if number%i == 0:
                return False
            if number%(i+2) == 0:
                return False
            i = i+6
    return True

def main():
    start_time = timeit.default_timer()
    total = 5
    limit = 2000000
    i = 5
    while i <= limit:
        if isPrime(i):
            total = total + i
        i = i+2
        if i <= limit and isPrime(i):
            total = total+i
        i = i+4
    elapsed = timeit.default_timer() - start_time
    print total
    print elapsed

if __name__ == '__main__':
    main()
