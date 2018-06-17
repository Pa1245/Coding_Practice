'''def palindrome(n, c):
    ps = ""
    cl = len(c)
    i = 0
    for i in range(n/2):
        ps = ps+c[i%cl]
    ps = ps+ps[::-1]
    if n%2 != 0:
        ps = ps[:n//2]+c[(i+1)%cl]+ps[n//2:]
    return ps

print(palindrome(9, "abcd"))'''

palindrome = lambda n, s: (s+s[-1-n%2::-1]).center(n, s[0])
