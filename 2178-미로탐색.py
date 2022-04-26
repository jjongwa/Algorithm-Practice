from collections import deque
import sys
input= sys.stdin.readline
N, M = map(int,input().split())
adj = []
for _ in range(N):
    adj.append(list(str(input())))

dy = (0,1,0,-1)
dx = (1,0,-1,0)

chk = [[0]*M for _ in range(N)]

def checkadj(y,x):
    if 0 <=y <M and 0<= x <N:
        return True

dq = deque()
def bfs(y, x, count):
    dq.append((y,x, count))
    chk[x][y] = 1
    while dq:
        ny, nx, nxtcount = dq.popleft()
        if nx == N-1 and ny == M-1:
            return nxtcount            
        for i in range(4):
            newy, newx = ny+dy[i], nx+dx[i]            
            if checkadj(newy, newx) and chk[newx][newy] == 0  and adj[newx][newy] == '1':
                dq.append((newy,newx, nxtcount+1))
                chk[newx][newy] = 1
            
print(bfs(0,0,1))