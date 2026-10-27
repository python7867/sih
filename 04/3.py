lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def winner(b):
    for l in lines:
        if b[l[0]] != ' ' and b[l[0]] == b[l[1]] == b[l[2]]:
            return b[l[0]]
    return ' '

def evaluate(b):
    if winner(b) == 'X': return 1
    if winner(b) == 'O': return -1
    return 0

def done(b):
    return winner(b) != ' '

def moves(b, maxi):
    m = 'X' if maxi else 'O'
    r = []
    for i in range(9):
        if b[i] == ' ':
            c = list(b)
            c[i] = m
            r.append(c)
    return r

def minimax(b, d, maxi, a, be):
    if d == 0 or done(b):
        return evaluate(b)
    ch = moves(b, maxi)
    if len(ch) == 0:
        return evaluate(b)
    if maxi:
        best = -1000
        for c in ch:
            best = max(best, minimax(c, d-1, False, a, be))
            a = max(a, best)
            if a >= be: break
        return best
    else:
        best = 1000
        for c in ch:
            best = min(best, minimax(c, d-1, True, a, be))
            be = min(be, best)
            if a >= be: break
