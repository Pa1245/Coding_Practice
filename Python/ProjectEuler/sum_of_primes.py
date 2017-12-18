import math

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
    total = 2
    for i in range(1, 2*int(math.pow(10, 6)), 2):
        if isPrime(i):
            total = total + i
    print total

if __name__ == '__main__':
    main()
