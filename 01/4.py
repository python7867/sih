lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def value(b):
    t = 0
    for l in lines:
        x = 0
        o = 0
        for k in range(3):
            if b[l[k]] == 'X': x += 1
            if b[l[k]] == 'O': o += 1
        if o == 0: t += x * x
        if x == 0: t -= o * o
    return t

def neighbours(b):
    r = []
    for i in range(9):
        if b[i] == ' ':
            c = list(b)
            c[i] = 'X'
            r.append(c)
    return r

cur = [' ',' ',' ',' ','O',' ',' ',' ',' ']

print("start value:", value(cur))

best = cur
best_val = value(cur)
for nb in neighbours(cur):
    if value(nb) > best_val:
        best_val = value(nb)
        best = nb
cur = best

print("final value:", value(cur))
print("board:", cur)
