N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int,input().split())))

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        tmp = field[i][j]
        
        if i == N-1 and j == N-1:
            print(dp[i][j])

        if j + tmp <N:
            dp[i][j+tmp] += dp[i][j]
        if i + tmp <N:
            dp[i+tmp][j] += dp[i][j]



'''
stack = []

stack.append([0,0,field[0][0]])
ans = 0

while stack:
    now = stack.pop()
    #print(now)
    # 오른쪽으로
    if now[2] == 0:
        ans += 1
        continue
    tmp = now[1] + now[2]
    if tmp < N:
        stack.append([now[0], tmp, field[now[0]][tmp]])
    # 아래로
    tmp = now[0]+ now[2]
    if tmp < N:
        stack.append([tmp, now[1], field[tmp][now[1]]])

print(ans)
'''