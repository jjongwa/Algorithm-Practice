import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N, M = map(int, input().split())
warp = []
for _ in range(N+M):
    a, b = map(int, input().split())
    warp.append((a,b))

visited = [0 for _ in range(101)]
dq = deque([1])


while dq:
    now = dq.popleft()   
    for i in range(1, 7):
        if now + 1 <= 100 and visited[now+1] == 0:
            nxt = now + i
            visited[nxt] = visited[now]+ 1
            if nxt in warp:
                visited[warp[nxt]] = visited[now] + 1
                dq.append(warp[nxt])
            else:
                dq.append(nxt)

    if visited[100]:
        print(visited[100])
        break            






    
