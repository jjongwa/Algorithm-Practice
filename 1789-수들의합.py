S =int(input())
mid = int(S**(1/2))

lo = 0
hi = S
ans = 0

def is_possible(mid):
    return mid*(mid+1)//2 <=S

while lo <= hi:
    #print(lo,hi)
    if is_possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1
    mid = (lo + hi) // 2
print(ans)