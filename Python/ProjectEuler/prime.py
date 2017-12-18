import math

def isPrime(number):
    '''limit = int(math.sqrt(number))
    if all(number%i != 0 for i in range(2, number)):
        return True
    return False
    '''
    if number == 1:
        return False
    elif number < 4:
        return True
    elif number%2 == 0:
        return False
    elif number < 9:
        return True
    elif number%3 == 0:
        return False
    else:
        r = int(math.sqrt(number))
        f = 5
        while f <= r:
            if number%f == 0:
                return False
            if number%(f+2) == 0:
                return False
            f = f+6
    return True

def main():
    '''n = 10001
    count = 0
    i = 2
    while True:
        if isPrime(i):
            count = count+1
            if count == n:
                print i
                break
        i = i+1
    '''
    limit = 10001
    count = 1
    possiblePrime = 1
    while True:
        possiblePrime = possiblePrime + 2
        if isPrime(possiblePrime):
            count = count+1
            if count == limit:
                print possiblePrime
                break


if __name__ == '__main__':
    main()
