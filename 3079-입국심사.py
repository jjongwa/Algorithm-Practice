N, M = map(int, input().split())
test = [int(input()) for _ in range(N)]

lo, hi = min(test), max(test)*M

def is_possible(mid):
    cnt = 0
    for t in test:
        cnt += mid//t
    return cnt >= M
ans = hi
while lo <= hi:
    mid = (lo + hi) // 2
    if is_possible(mid):
        hi = mid - 1
        ans = mid
    else:
        lo = mid + 1
    mid = (lo + hi) // 2

print(ans)