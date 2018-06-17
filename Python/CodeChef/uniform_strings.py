def main():
    t = int(raw_input())
    while t > 0:
        string = raw_input()
        transitions = 0
        flag = False
        if string[0] == string[-1]:
            flag = True
            for i in range(1, len(string)):
                if string[i-1] != string[i]:
                    transitions = transitions+1
        if flag and transitions <= 2:
            print 'uniform'
        else:
            print 'non-uniform'
        t = t-1

if __name__ == '__main__':
    main()
