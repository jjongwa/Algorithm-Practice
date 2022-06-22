import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N = int(input())
place = [list(map(int, input().split()))for _ in range(N)] 

for i in range(N):
    for j in range(N):
        if place[i][j] == 9:
            shark = (i, j)

dx = (-1,0,0,1)
dy = (0,-1,1,0)

def is_possible(x, y, lv):
    return 0<=x<N and 0<=y<N and lv >= place[x][y]

def bfs(x,y, lv, lv_cnt, cnt, chk):
    dq = deque()
    dq.append((x,y,lv,lv_cnt, cnt,chk))
    cct = 0
    while dq:
        now_x, now_y, now_lv, now_lv_cnt, now_cnt, now_chk = dq.popleft()
        if place[now_x][now_y] < now_lv:
            now_lv_cnt += 1
            if now_lv_cnt == now_lv:
                now_lv += 1
                now_lv_cnt = 0
            return (1, now_x, now_y, now_lv, now_lv_cnt, now_cnt, now_chk)
        for i in range(4):
            nx, ny = now_x+dx[i], now_y+dy[i]
            if is_possible(nx,ny, now_lv) and chk[nx][ny] == 0:
                now_chk[nx][ny] = 1
                dq.append((nx, ny, now_lv, now_lv_cnt, now_cnt+1,now_chk))
    return (0, now_x, now_y, now_lv, now_lv_cnt, now_cnt, now_chk)

ans = 0
check = [[0 for _ in range(N)] for _ in range(N)]
triger, x, y, lv, lv_cnt, count, chk = bfs(shark[0], shark[1], 2, 0, 0, check)

while True:
    if triger == 1:
        ans += count
        triger, x, y, lv, lv_cnt, count, chk  = bfs(x, y, lv, lv_cnt, count, chk)
        print(x, y)
    else:
        print(ans)
        break



