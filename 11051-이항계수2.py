import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**7)

MOD = 10007
N, K = map(int, input().split())

# recursion with memoization
cache = [[0] * 1001 for _ in range(1001)]
def bino(n, k):
    if cache[n][k]:
        return cache[n][k]
    if n == k or k == 0:
        cache[n][k] = 1
    else:
        cache[n][k] = (bino(n-1, k-1) + bino(n-1, k)) % MOD
    return cache[n][k]

print(bino(N,K))

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = (cache[i-1][j-1] + cache[i-1][j]) % MOD
    
print(cache[N][K])

# 내 풀이
'''
dp = [[1 for _ in range(n+1)] for n in range(N+1)]

for n in range(N+1):
    for k in range(n+1):
        if k != 0 and n != k:
            dp[n][k] = (dp[n-1][k-1] + dp[n-1][k]) % 10007
print(dp[N][K])
'''
