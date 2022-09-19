import sys
sys.setrecursionlimit(10**7)
INT_MAX = sys.maxsize
n, m  = map(int, input().split())
coinList = list(map(int, input().split()))

dp = [INT_MAX for _ in range(m+1)]
dp[0] = 0

def dpdp(st):
    for c in coinList:
        if st+c > m:
            continue
        dp[st+c] = min(dp[st+c], dp[st]+1)
        dpdp(st+c)

dpdp(0)

ans = dp[m]
if ans == INT_MAX:
    ans = -1
print(ans)
