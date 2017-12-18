import math

def main():
    lastNumber = 100
    sumOfSquare = 0
    squareOfSum = 0

    #Brute Force method - Inefficient for large numbers
    '''for i in range(1, lastNumber+1):
        sumOfSquare = sumOfSquare + math.pow(i, 2)
        squareOfSum = squareOfSum + i
    squareOfSum = math.pow(squareOfSum, 2)'''

    # efficient method
    squareOfSum = (lastNumber/2)*(lastNumber+1)
    sumOfSquare = (lastNumber*(2*lastNumber+1)*(lastNumber+1))/6
    print squareOfSum
    print sumOfSquare
    print math.fabs(math.pow(squareOfSum, 2) - sumOfSquare)

if __name__ == '__main__':
    main()
