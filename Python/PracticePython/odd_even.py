def main():
    number = int(raw_input("Enter an integral number: "))
    if(number%2 == 0):
        print("You entered an even number.")
        if(number%4 == 0):
            print("You entered a multiple of 4.")
    else:
        print("You entered an odd number.")

if __name__ == '__main__':
    main()
