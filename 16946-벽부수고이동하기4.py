import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())
adj =[]
for _ in range(N):
    adj.append(list(str(input().strip())))

dy = (0,1,0,-1)
dx = (1,0,-1,0)

def chkadj(x, y):
    if 0<= x < N and 0<= y < M:
        return True


def bfs(x, y, cnt):
    count = 1
    dq = deque()
    dq.append((x,y))
    chk[x][y] = cnt
    while dq:
        nowx, nowy = dq.popleft()
        for i in range(4):
            nx, ny = nowx+dx[i], nowy+dy[i]
            if chkadj(nx,ny) and chk[nx][ny] != cnt and adj[nx][ny] != '1' :
                if adj[nx][ny] != '0':
                    return (adj[nx][ny])
                count += 1
                chk[nx][ny] = cnt
                dq.append((nx,ny))
    return (cnt,count)

chk = [[0]*M for _ in range(N)]    
cnt = 1
for i in range(N):
    for j in range(M):
        if adj[i][j] != '1':
            adj[i][j] = bfs(i,j,cnt)
            cnt += 1

ans = [[]for _ in range(N)]
for x in range(N):
    for y in range(M):
        if adj[x][y] == '1':
            tmp = []
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if chkadj(nx,ny) and adj[nx][ny] != '1' and adj[nx][ny] not in tmp:
                    tmp.append(adj[nx][ny])            
            sumtmp= 0
            #print(tmp)
            for i in tmp:
                sumtmp += i[1]
            ans[x].append(int(sumtmp+1)%10)
        else:
            ans[x].append(0)
        
for i in range(N):
    for j in range(M):
        print(ans[i][j], end='')
    print()


'''
for i in range(N):
    for j in range(M):
        if adj[i][j] == '1':
            adj[i][j] = -1

#print(adj)
dy = (0,1,0,-1)
dx = (1,0,-1,0)

def chkadj(x, y):
    if 0<= x < N and 0<= y < M:
        return True

def bfs(x, y, cnt):
    count = 1
    dq = deque()
    dq.append((x,y))
    chk[x][y] = cnt
    while dq:
        nowx, nowy = dq.popleft()
        for i in range(4):
            nx, ny = nowx+dx[i], nowy+dy[i]
            if chkadj(nx,ny) and chk[nx][ny] != cnt and adj[nx][ny] != '1' :
                if adj[nx][ny] != '0':
                    return adj[nx][ny]
                count += 1
                chk[nx][ny] = cnt
                dq.append((nx,ny))
    return count

chk = [[0]*M for _ in range(N)]    
cnt = 1
for i in range(N):
    for j in range(M):
        if adj[i][j] == '0':
            adj[i][j] = bfs(i,j,cnt)
            cnt += 1
#print(adj)


ans = [[]for _ in range(N)]
for x in range(N):
    for y in range(M):
        if adj[x][y] == '1':
            tmp = 0
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if chkadj(nx,ny) and adj[nx][ny] != '1':
                    tmp += adj[nx][ny]
            ans[x].append(tmp+1)
        else:
            ans[x].append(0)

for i in range(N):
    for j in range(M):
        print(int(int(ans[i][j])%10), end='')
    if i != N-1:
        print()


def bfs(x, y, cnt):
    count = 1
    dq = deque()
    dq.append((x,y))

    while dq:
        nowx, nowy = dq.popleft()
        for i in range(4):
            nx, ny = nowx+dx[i], nowy+dy[i]
            if chkadj(nx,ny) and chk[nx][ny] != cnt and adj[nx][ny] == '0' :
                count += 1
                chk[nx][ny] = cnt
                dq.append((nx,ny))

    return count % 10

ans = [[] for _ in range(N)]
chk = [[0]*M for _ in range(N)]
cnt = 1
for i in range(N):
    for j in range(M):
        if adj[i][j] == '0':
            ans[i].append(0)
        else:
            ans[i].append(bfs(i,j,cnt))
            cnt += 1

for i in range(N):
    for j in range(M):
        print(ans[i][j], end='')
    print()

'''
