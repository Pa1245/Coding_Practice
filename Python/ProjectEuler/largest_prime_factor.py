# Description: To find the largest prime factor of a given number.
# Author: Parag Amrutkar

import math
import logging
logging.basicConfig(Level = logging.DEBUG)

# Return the factors of given integer as a list
def findFactors(number):
    factors = []
    for i in range(1, int(math.sqrt(number) + 1)):
        if number%i == 0:
            factors.append(i)
            factors.append(number//i)
    return factors

# Check if the number is prime or not
def isPrime(number):
    return len(findFactors(number)) == 2

# Print largest prime factor
factors = findFactors(600851475143)
largestPrimeFactor = 1
for factor in factors:
    if isPrime(factor) and factor>largestPrimeFactor:
        largestPrimeFactor = factor

print(largestPrimeFactor)
