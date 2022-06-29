import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
from collections import deque

dx = (1,1,2,2,-1,-1,-2,-2)
dy = (2,-2,1,-1,2,-2,1,-1)

def is_possible(x, y):
    global l
    return 0 <= x < l and 0 <= y < l

T = int(input())
for _ in range(T):
    l = int(input())
    x, y = map(int, input().split())
    px, py = map(int, input().split())
    if x == px and y == py:
        print(0)
        continue

    dq = deque()
    chk = [[0 for _ in range(l)] for _ in range(l)]

    dq.append((x,y,0))
    chk[x][y] = 1
    tri = 0
    while dq:
        nowx, nowy, nowcnt = dq.popleft()
        for i in range(8):
            nx, ny = nowx+dx[i], nowy+dy[i]
            if nx == px and ny == py:
                ans = nowcnt+1
                tri = 1
                break
            if is_possible(nx,ny) and chk[nx][ny] == 0:
                chk[nx][ny] = 1
                dq.append((nx, ny, nowcnt+1))            
        if tri:
            break
    print(ans)