'''def lcm(x, y):
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if (greater%x == 0) and (greater%y == 0):
            lcm = greater
            break
        greater = greater+1
    return lcm

def main():
    number = 20
    smallestMultiple = number
    while number>1:
        if smallestMultiple%number == 0:
            number = number-1
        else:
            smallestMultiple = lcm(smallestMultiple, number)
            number = number-1
    print smallestMultiple
'''
import math
def primeList(x, y):
    primeNumbers = []
    for num in range(x, y+1):
        if all(num%i != 0 for i in range(2, num)):
            primeNumbers.append(num)
    return primeNumbers

def main():
    lastNumber = 20
    primeNumbers = primeList(2, lastNumber)
    powers = [1]*len(primeNumbers)
    smallestMultiple = 1
    index = 0
    check = True
    limit = math.sqrt(lastNumber)
    while index < len(primeNumbers):
        if check:
            if primeNumbers[index] <= limit:
                powers[index] = int(math.log(lastNumber)/math.log(primeNumbers[index]))
            else:
                check = False
        smallestMultiple = smallestMultiple * int(math.pow(primeNumbers[index], powers[index]))
        index = index+1
    print primeNumbers
    print powers
    print smallestMultiple

if __name__ == '__main__':
    main()
