N, M = map(int, input().split())
trees = list(map(int,input().split()))

lo = 0
hi = max(trees)
mid = (lo+ hi) //2

def is_possible(mid):
    tmp = 0
    for t in trees:
        if t > mid:
            tmp += (t-mid)
    #print(tmp)
    return tmp >= M
ans = 0
while lo <= hi:    
    #print(lo, mid, hi)
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid -1
    mid = (lo+ hi) //2
print(ans)