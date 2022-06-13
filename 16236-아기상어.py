import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N = int(input())
place = [list(map(int, input().split()))for _ in range(N)] 

for i in range(N):
    for j in range(N):
        if place[i][j] == 9:
            shark = (i, j)

dx = (-1,0,1,0)
dy = (0,-1,0,1)

def is_possible(x, y, lv):
    return 0<=x<N and 0<=y<N and lv >= place[x][y]


def bfs(x, y, cnt, lv, eat, limit):
    dq = deque()
    dq.append((x, y, cnt, lv, eat, limit))  #   count, level, eat, limit
    check = [[0 for _ in range(N)] for i in range(N)]
    check[x][y] = 1
    while dq:
        x, y, cnt, lv, eat, limit = dq.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if is_possible(nx,ny, lv) and check[nx][ny] == 0:
                if 0 < place[nx][ny] < lv:
                    eat += 1
                    if eat == lv:
                        lv += 1
                        eat = 0
                    return (nx, ny, cnt+limit+1, lv, eat, 0)
                else:
                    dq.append((nx, ny, cnt, lv, eat, limit + 1))
                    check[nx][ny] = 1
    print(">")
    return -1

ans = 0
way = bfs(shark[0], shark[1], 0, 2, 0, 0)
while True:
    print(way) 
    if way == -1:
        print(ans)
        exit(0)
        break
    else:
        way = bfs(way[0], way[1], way[2], way[3], way[4], way[5])
        ans += way[2]