'''
# BFS 버전
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
field = [[False] * 1001 for _ in range(1001)]
for _ in range(M):
    x, y = map(int, input().split())
    field[x][y] = True
    field[y][x] = True

chk =  [False]* 1001

def bfs(start):
    dq = deque()
    dq.append(start)
    while dq:
        now  = dq.popleft()
        if chk[now]:
            continue
        else:
            chk[now] = True
            for nxt in range(1, 1001):
                if field[now][nxt]:
                    dq.append(nxt)
ans = 0
for i in range(1, N+1):
    if chk[i] == False:
        ans += 1
        bfs(i)

print(ans)
'''

# DFS 버전
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N, M = map(int, input().split())
field = [[False] * 1001 for _ in range(1001)]
for _ in range(M):
    x, y = map(int, input().split())
    field[x][y] = True
    field[y][x] = True

chk =  [False]* 1001

def dfs(start):
    #chk[start] = True
    for nxt in range(1, 1001):
        if field[start][nxt] and chk[nxt] == False:
            chk[nxt] = True
            dfs(nxt);

ans = 0
for i in range(1, N+1):
    if chk[i] == False:
        ans+=1
        chk[i] = True
        dfs(i)
print(ans)
