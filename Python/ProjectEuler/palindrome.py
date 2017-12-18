import timeit

def reverse(number):
    temp = 0
    i = 0
    while(number != 0):
        temp = 10*temp + (number%10)
        number = number/10
        i = i+1
    return temp

def isPalindrome(number):
    return number == reverse(number)

def isDivisibleby3Digit(number):
    for i in range(100, 1000):
        if number%i == 0:
            if (number/i >= 100) and (number/i < 1000):
                print str(i) + " & " + str(number/i)
                return True
    return False

def main():
    starttime = timeit.default_timer()
    for i in range(999*999, 100*100-1, -1):
        if isPalindrome(i):
            if(isDivisibleby3Digit(i)):
                print i
                break
    elapsed = timeit.default_timer() - starttime
    print "time needed = " + str(elapsed)
'''def main():
    starttime = timeit.default_timer()
    largestPalindrome = 0
    for i in range(999, 99, -1):
        j = 999
        while j >= i:
            number = i*j
            if isPalindrome(number) and (number > largestPalindrome):
                largestPalindrome = number
                break
            j = j-1
    print largestPalindrome
    elapsed = timeit.default_timer() - starttime
    print elapsed'''

if __name__ == "__main__":
    main()
