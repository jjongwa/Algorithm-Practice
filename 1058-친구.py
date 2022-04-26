import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
adj = []
for _ in range(N):
    adj.append(list(input().strip()))

def bfs(start, line):
    dq = deque()
    dq.append((start,line))
    chk[start] = 1
    while dq:
        now, nowline = dq.popleft()        
        if nowline == 2:
            continue
        for nxt in range(N):
            if adj[now][nxt] == 'Y' and chk[nxt] == 0:
                chk[nxt] = 1
                dq.append((nxt,nowline+1))

ans = 0
for i in range(N):
    chk = [0] * N
    bfs(i,0)
    ans = max(ans, sum(chk)-1)

print(ans)