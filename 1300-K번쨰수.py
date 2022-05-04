N = int(input())
k = int(input())

lo, hi = 1, N*N



def is_possible(cnt):
    return cnt < k

while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(mid//i, N)

    if is_possible(cnt):
        lo = mid + 1
    else:
        hi = mid - 1
print(lo)