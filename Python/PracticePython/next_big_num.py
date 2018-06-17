# Create a function that takes a positve integer bumber and returns the next
# bigger number formed by the same digitsself.

import itertools

def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2, -1, -1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

print next_bigger(235)
