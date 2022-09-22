n = int(input())
dp = [-1 for _ in range(n+1)]
dp[1] = 1
dp[2] = 3

for i in range(3,n+1):
    dp[i] = (dp[i-1] + 2* dp[i-2]) % 10007

print(dp[n])

'''
def fill(now):
    if dp[now] != -1:
        return dp[now]
    if now < 1:
        return 0 
    dp[now] = (fill(now-1) + 2*fill(now-2)) % 10007
    return dp[now]

print(fill(n))
'''