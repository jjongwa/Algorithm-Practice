#   Á¦°ö¼öÀÇ ÇÕ
'''
N = int(input())
ansList = [x for x in range(N+1)]
for i in range(1,N+1):
    for j in range(1,i):
            if j*j >i:
                break
            if ansList[i] > ansList[i-j*j] +1:
                ansList[i] = ansList[i-j*j] +1

#print(int(N**(1/2))**2)
print(ansList[N])
'''
import sys
import math

N = int(sys.stdin.readline())
dp = [0]*(N+1)

for i in range(1,N+1):
    dp[i] = i
    for j in range(1,int(math.sqrt(i)+1)):
        if dp[i] > dp[i-j*j]+1:    
            dp[i] = dp[i-j*j]+1
print(dp[N])