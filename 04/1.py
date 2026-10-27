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
