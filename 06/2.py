from collections import deque

D = {'A': {'R'}, 'B': {'R','G','B'},
     'C': {'R','G','B'}, 'D': {'R','G','B'}}

N = {'A': ['B','C'], 'B': ['A','C','D'],
     'C': ['A','B','D'], 'D': ['B','C']}

def revise(x, y):
    old = D[x].copy()

    for a in old:
        if all(a == b for b in D[y]):
            D[x].remove(a)

    return old != D[x]


def ac3():
