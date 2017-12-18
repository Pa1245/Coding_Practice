import math

def main():
    for a in range(1, 1000):
        for b in range(a, 1000-a):
            c = 1000-a-b
            if c**2 == a**2 + b**2:
                print(a, b, c, a*b*c)

if __name__ == "__main__":
    main()
