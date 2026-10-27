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
    q = deque((x, y) for x in N for y in N[x])

    while q:
        x, y = q.popleft()

        if revise(x, y):
            if not D[x]:
                return False

            for z in N[x]:
                if z != y:
                    q.append((z, x))

    return True

print("Consistent:", ac3())
print("Domains:", D)


