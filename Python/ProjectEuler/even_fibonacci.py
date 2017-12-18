# Description: To find the sum of even terms in fibonacci series upto 4 million
# Author: Parag Amrutkar

def main():
    first_term = 1
    second_term = 2

    total = 0

    while(second_term <= 4000000):
        if second_term%2 == 0:
            total = total + second_term
        temp = second_term
        second_term = second_term + first_term
        first_term = temp

    print total

if __name__ == '__main__':
    main()
