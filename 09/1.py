from sympy import Symbol, And

pr = [
    ("ram", "sita"),
    ("ram", "arjun"),
    ("sita", "priya"),
    ("mohan", "ram")
]

def par(x, y):
    return (x, y) in pr
