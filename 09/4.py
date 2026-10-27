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

print("ram parent of sita:", par("ram", "sita"))
print("mohan grandparent of sita:", gp("mohan", "sita"))
print("ram grandparent of priya:", gp("ram", "priya"))
print("children of ram:", child("ram"))
print("siblings of sita:", sib("sita"))

P = Symbol("parent")
G = Symbol("grandparent")
expr = And(P, G)
print("expression:", expr)
