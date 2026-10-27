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
