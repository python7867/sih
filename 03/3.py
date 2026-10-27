import random
import math

goal = [1,2,3,4,5,6,7,8,0]
start = [1,2,3,4,0,6,7,5,8]

def expand(s):
    r = []
    b = s.index(0)
    for t in [b-3, b+3, b-1, b+1]:
        if 0 <= t < 9 and not (b % 3 == 0 and t == b-1) and not (b % 3 == 2 and t == b+1):
            c = list(s)
            c[b], c[t] = c[t], c[b]
            r.append(c)
    return r

def simulate(s):
    c = list(s)
    for st in range(20):
        if c == goal:
            return 1
        k = expand(c)
        c = k[random.randint(0, len(k) - 1)]
    return 0

def make_node(s, p):
    return {'state': s, 'parent': p, 'children': [], 'visits': 0, 'total': 0.0}

def ucb(c, pv):
    if c['visits'] == 0:
        return 1000000
    return c['total']/c['visits'] + 1.4*math.sqrt(math.log(pv)/c['visits'])

root = make_node(start, None)
for it in range(2000):
    n = root
    while len(n['children']) > 0:
        best = n['children'][0]
        for ch in n['children']:
            if ucb(ch, n['visits']) > ucb(best, n['visits']):
                best = ch
        n = best
    if n['visits'] > 0:
        for s in expand(n['state']):
            n['children'].append(make_node(s, n))
