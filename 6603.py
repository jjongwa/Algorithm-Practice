from collections import deque
from itertools import combinations
''' 
while True:
    lotto = deque(map(int,input().split()))
    if lotto[0] == 0:
        break
    k = lotto[0]
    lotto.popleft()
    #print(lotto)
    
    s = list(combinations(lotto,6))
    for i in s:
        for j in i:
            print(j,end=' ')
        print()

    print()
'''
combi = [0 for i in range(6)]

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()