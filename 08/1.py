n = 4
board = [-1] * n

def solve(row):
    if row == n:
        return True

    for col in range(n):
