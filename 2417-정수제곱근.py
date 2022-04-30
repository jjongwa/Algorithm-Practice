n =int(input())
if n == 0:
    print(0)
    exit(0)
def is_possible(mid):
    return mid**2 <n

lo = 0
hi = n
while lo <= hi:
    mid = (lo + hi) //2
    if is_possible(mid):
        lo = mid+1
    else:
        hi = mid -1
    
print(lo)