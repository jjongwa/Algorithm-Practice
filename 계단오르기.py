n = int(input())
dp = [0 for _ in range(n+4)]
dp[0] = 1

for i in range(0, n-1):
    dp[i+2] += dp[i]
    dp[i+3] += dp[i]

print(dp[n]%10007)
