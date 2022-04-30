from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
zerospot = []
for x in range(N):
    for y in range(M):
        if board[x][y] == 0:
            zerospot.append((x,y))
bruteList = list(combinations(zerospot,3))  # 막을 위치 combi로 추출

dy = (0,1,0,-1)
dx = (1,0,-1,0)

def is_valid_coord(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(arr, x, y):
    dq = deque()
    dq.append((x,y))
    while dq:
        nowx, nowy = dq.popleft()
        for i in range(4):
            nx, ny = nowx+dx[i], nowy+dy[i]
            if is_valid_coord(nx,ny) and arr[nx][ny] == 0:
                arr[nx][ny] = 3
                dq.append((nx,ny)) 

ans = 0
for block in bruteList:
    tmpboard = copy.deepcopy(board)     # 깊은복사
    for i in range(3):
        tmpboard[block[i][0]][block[i][1]] = 1
    
    for x in range(N):
        for y in range(M):
            if tmpboard[x][y] == 2:
                bfs(tmpboard, x, y)
    
    cnt = 0
    for x in range(N):
        for y in range(M):
            if tmpboard[x][y] == 0:
                cnt += 1
    ans = max(ans, cnt)
print(ans)



