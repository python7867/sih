import random
import math

cities = [[0,0],[1,5],[5,2],[6,6],[8,3],[2,8]]

def cost(t):
    total = 0
    for i in range(len(t)):
        a = cities[t[i]]
        b = cities[t[(i + 1) % len(t)]]
        total += math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return total

def neighbour(t):
    c = list(t)
    i = random.randint(0, len(c) - 1)
    j = random.randint(0, len(c) - 1)
    c[i], c[j] = c[j], c[i]
    return c

cur = [0, 1, 2, 3, 4, 5]
best = cur
temp = 100.0
cool = 0.99

print("start cost:", round(cost(cur), 2))

while temp > 0.01:
    nb = neighbour(cur)
