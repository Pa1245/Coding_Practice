import timeit

term_arr = [0]*1000000
term_arr[1] = 1
term_arr[0] = 1

def num_of_terms(number):
    if number < 1000000:
        if term_arr[number] == 0:
            if number % 2 == 0:
                return 1 + num_of_terms(number/2)
            else:
                return 1 + num_of_terms(3*number + 1)
        return term_arr[number]
    else:
        if number % 2 == 0:
            return 1 + num_of_terms(number/2)
        else:
            return 1 + num_of_terms(3*number + 1)

def main():
    start_time = timeit.default_timer()
    longest_chain = [1, 1]
    temp = 1
    for i in range(2, 1000000):
        temp = num_of_terms(i)
        if temp > longest_chain[1]:
            longest_chain[1] = temp
            longest_chain[0] = i
    print longest_chain
    elapsed_time = timeit.default_timer() - start_time
    print elapsed_time

if __name__ == "__main__":
    main()
