def safe(b, r, c, n):
    for co in range(3):
        if b[r][co] == n:
            return False
    for ro in range(3):
        if b[ro][c] == n:
            return False
    return True

