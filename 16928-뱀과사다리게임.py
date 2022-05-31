import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N, M = map(int, input().split())
warp = {}
for _ in range(N+M):
    a, b = map(int, input().split())
    warp[a] = b

visited = [0 for _ in range(101)]
board = [0 for _ in range(101)]
dq = deque([1])


while dq:
    now = dq.popleft()   
    for i in range(1, 7):
        if now + i <= 100 and visited[now+i] == 0:
            nxt = now + i
            if nxt in warp:
                nxt = warp[nxt]
            if visited[nxt] == 0:
                visited[nxt] = 1
                board[nxt] = board[now]+ 1
                dq.append(nxt)
    if now == 100:
        print(board[100])
        break            






    
