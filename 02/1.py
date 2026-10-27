import random
import math

cities = [[0,0],[1,5],[5,2],[6,6],[8,3],[2,8]]

def cost(t):
    total = 0
    for i in range(len(t)):
        a = cities[t[i]]
        b = cities[t[(i + 1) % len(t)]]
