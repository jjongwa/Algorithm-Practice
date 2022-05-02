K, N = map(int, input().split())
lan = list(int(input()) for _ in range(K)) 

lo = 1
hi = sum(lan) // N
#print(hi)
def is_possible(mid):
    cnt = 0
    for i in lan:
        cnt += (i // mid)
    
    return cnt >= N
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    #print(lo, hi, mid)
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1
    mid = (lo + hi) // 2

print(ans)