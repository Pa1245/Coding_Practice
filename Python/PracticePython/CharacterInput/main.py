from datetime import date

def main():
    name = raw_input("What is your name: ")
    age = int(raw_input("How old are you: "))
    year = str((date.today().year - age)+100)
    message = name + " will be 100 years old in the year " + year
    print(message)
    numberOfCopies = int(raw_input("How many times should the previous message be printed? "))
    print (message+'\n')*numberOfCopies

if __name__ == '__main__':
    main()
