from sympy import Symbol, And

pr = [
    ("ram", "sita"),
    ("ram", "arjun"),
    ("sita", "priya"),
    ("mohan", "ram")
]

def par(x, y):
    return (x, y) in pr

def child(x):
    return [c for p, c in pr if p == x]

def gp(x, y):
    for p, c in pr:
        if p == x and par(c, y):
            return True
    return False

def sib(x):
    r = set()
    for p, c in pr:
        if c == x:
            for op, oc in pr:
                if op == p and oc != x:
                    r.add(oc)
    return sorted(r)

for p, c in pr:
    print(p, "parent of", c)

