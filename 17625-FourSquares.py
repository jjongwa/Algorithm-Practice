import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations
n = int(input())

square = [x**2 for x in range(int(n**(1/2))+1)]
#print(square)

dp = [0] * (n+1)
dp[0], dp[1] = 0, 1

for i in range(2, n+1):
    if i in square:
        dp[i] = 1
    else:
        dp[i] = i

for i in range(2, n+1):
    for j in range(2, int(i**(1/2))):
        dp[i] = min(dp[i], dp[j*j]+dp[i-j*j])

print(dp[n])
