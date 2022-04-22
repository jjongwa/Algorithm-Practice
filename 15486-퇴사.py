import sys
input = sys.stdin.readline
N = int(input())
sch = [list(map(int,input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]
tmp = 0
for i in range(N):
    tmp = max(tmp, dp[i])
    if i + sch[i][0] > N:
        continue
    dp[i+ sch[i][0]] = max(tmp+sch[i][1], dp[i+sch[i][0]])

#print(dp)
print(max(dp))