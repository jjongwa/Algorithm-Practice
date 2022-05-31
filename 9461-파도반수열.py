import sys
sys.stdin = open('input.txt', 'r')
dp = [0 for _ in range(101)]
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5]  = 2

for i in range(6, 101):
    dp[i] = dp[i-5] + dp[i-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])