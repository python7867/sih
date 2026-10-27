def safe(b, r, c, n):
    for co in range(3):
        if b[r][co] == n:
            return False
    for ro in range(3):
        if b[ro][c] == n:
            return False
    return True

def solve(b):
    for r in range(3):
        for c in range(3):
            if b[r][c] == 0:
                for n in range(1, 4):
                    if safe(b, r, c, n):
                        b[r][c] = n
                        if solve(b):
                            return True
                        b[r][c] = 0
                return False
    return True

b = [[1, 0, 3],
     [0, 3, 0],
     [0, 0, 2]]

print("original:")
for row in b:
    print(row)

if solve(b):
    print("\nsolution:")
    for row in b:
        print(row)
else:
    print("no solution")
