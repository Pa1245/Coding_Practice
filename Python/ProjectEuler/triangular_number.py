from math import sqrt

def num_of_divisors(num):
    total_divisors = 0
    cross_limit = sqrt(num)
    if int(cross_limit) == cross_limit:
        total_divisors = -1
    for i in range(1, int(cross_limit)+1):
        if num%i == 0:
            total_divisors = total_divisors+2
    return total_divisors

def main():
    flag = False
    triang_num = 1
    i = 2
    while True:
        triang_num = triang_num + i
        if num_of_divisors(triang_num) > 500:
            print triang_num
            break
        i = i+1

if __name__ == '__main__':
    main()
