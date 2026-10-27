n = 4
board = [-1] * n

def solve(row):
    if row == n:
        return True

    for col in range(n):
        safe = True

        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(row - i):
                safe = False
                break

        if safe:
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

if solve(0):
    for r in range(n):
        print(" ".join("Q" if board[r] == c else "." for c in range(n)))
else:
    print("No solution")
