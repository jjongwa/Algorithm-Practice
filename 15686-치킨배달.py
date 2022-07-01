import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations

def dist(r1,c1,r2,c2):
    return abs(r1-r2) + abs(c1-c2)

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

house = []
chick = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            house.append((r,c))
        elif board[r][c] == 2:
            chick.append((r,c))

dist_list = [[0 for _ in range(len(chick))] for _ in range(len(house))]

for h in range(len(house)):
    for c in range(len(chick)):
        dist_list[h][c] += dist(house[h][0], house[h][1], chick[c][0], chick[c][1])

chkList = list(combinations(chick, M))
for i in range(len(chkList)):
    






'''
from itertools import combinations
from collections import deque
N, M = map(int, input().split())
board = []

dx = (0,1,0,-1)
dy = (1,0,-1,0)

def is_possible(x, y):
    return 0 <= x < N and 0 <= y < N

for _ in range(N):
    board.append(list(map(int, input().split())))

house = []
chick = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            house.append((r,c))
        elif board[r][c] == 2:
            chick.append((r,c))

ch = list(combinations(chick, M))

ansList =[]
newboard = board
for i in range(len(ch)):
    for r in range(N):
        for c in range(N):
            if newboard[r][c] == 2:
                newboard[r][c] = 0
    for j in range(len(ch[i])):
        newboard[ch[i][j][0]][ch[i][j][1]] = 2
    ans = 0
    for j in range(len(house)):
        dq = deque()
        dq.append((house[j][0],house[j][1], 0))
        chk = [[0 for _ in range(N)] for _ in range(N)]
        chk[house[j][0]][house[j][1]] = 1
        tri = 0
        while dq:
            x, y, cnt = dq.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if is_possible(nx,ny) and chk[nx][ny] == 0:
                    dq.append((nx, ny, cnt+ 1))
                    if newboard[nx][ny] == 2:
                        ans += (cnt+1)
                        tri = 1
                        break
            if tri:
                break
    ansList.append(ans)
print(min(ansList))
'''
