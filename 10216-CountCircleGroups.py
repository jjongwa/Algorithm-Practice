import sys
input = sys.stdin.readline
T = int(input())

def is_connect(a, b):
    ab =(enemy[a][0] - enemy[b][0])**2 + (enemy[a][1] - enemy[b][1])**2
    return ab <= (enemy[a][2]+enemy[b][2])**2

def dfs(nxt):
    for i in range(N):
        if chk[i] == 0 and is_connect(nxt, i):
            chk[i] = 1
            dfs(i)

for _ in range(T):
    N = int(input())
    enemy =[]
    for _ in range(N):
        enemy.append(list(map(int,input().split())))

    chk = [0 for _ in range(N)]
    cnt = 0
    for i in range(N):
        if chk[i] == 0:
            chk[i] = 1
            cnt += 1
            dfs(i)
    print(cnt)



