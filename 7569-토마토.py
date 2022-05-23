import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

M, N, H = map(int,input().split())
board = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

dx = (0, 0, 1, 0, 0, -1)
dy = (0, 1, 0, 0, -1, 0)
dz = (1, 0, 0, -1, 0, 0)

def is_possible(x, y, z):
    return 0 <= x < M and 0 <= y < N and 0 <= z < H
day = 0
dq = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if board[z][y][x] == 1:
                dq.append((z,y,x, day))
ans = 0

while dq:
    z, y, x, day = dq.popleft()
    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
        if is_possible(nx,ny,nz) and board[nz][ny][nx] == 0:
            board[nz][ny][nx] = day + 1
            ans = max(ans, day + 1)
            dq.append((nz,ny,nx, day+1))



for z in range(H):
    for y in range(N):
        for x in range(M):
            if board[z][y][x] == 0:
                ans = -1
if ans == 0:
    print(0)
else:    
    print(ans)

