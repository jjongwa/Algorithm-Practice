import sys
sys.setrecursionlimit(10**7)
INT_MAX = sys.maxsize
n, m  = map(int, input().split())
coinList = list(map(int, input().split()))

dp = [INT_MAX for _ in range(m+1)]
dp[0] = 0

for i in range(1,m+1):
    for j in range(n):
        if i >= coinList[j]: # j번째 동전의 값이 i 보다 작다 ==> 동전 사용 가능하다
            dp[i] = min(dp[i], dp[i - coinList[j]] + 1)

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])