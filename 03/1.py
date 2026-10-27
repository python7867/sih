import random
import math

goal = [1,2,3,4,5,6,7,8,0]
start = [1,2,3,4,0,6,7,5,8]

def expand(s):
    r = []
    b = s.index(0)
    for t in [b-3, b+3, b-1, b+1]:
        if 0 <= t < 9 and not (b % 3 == 0 and t == b-1) and not (b % 3 == 2 and t == b+1):
            c = list(s)
            c[b], c[t] = c[t], c[b]
            r.append(c)
    return r
