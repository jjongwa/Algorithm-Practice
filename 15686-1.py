"""
13 C M
13 C 7 = 1716
집: 최대 100군데
100  * 7 * 1716 = 1,201,200 
-> 부르트포스가 가능하다~
"""



import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations

N, M = map(int,input().split())
houses = []
chickens = []
for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i,j))
        elif v == 2:
            chickens.append((i,j))


print(houses)
print(chickens)            