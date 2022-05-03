import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
way =[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        way[i][j] = ((j-i)*(1+abs(A[i]-A[j])))
#print(way)
lo = 1
hi = max(A)
def is_possible(mid):
    dp = [1000000*N for _ in range(N)]
    for i in range(1,N):
        for j in range(i):
            #print(way[j][i], mid)
            if way[j][i] <= mid:
                dp[i] = min(way[0][i], dp[j]+way[j][i])
                #print(dp)
    return dp[N-1] != 1000000*N

ans = 0
while lo <=hi:
    mid = (lo+hi) // 2
    #print(lo, hi, mid)
    if is_possible(mid):
        hi = mid -1
        ans = mid
    else:
        lo = mid + 1
    mid = (lo+hi) // 2

print(ans)
