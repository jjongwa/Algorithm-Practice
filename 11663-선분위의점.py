from bisect import bisect_left, bisect_right
import sys
input= sys.stdin.readline
N, M = map(int, input().split())
dot = list(map(int, input().split()))
for _ in range(M):
    le, ri = map(int, input().split())
    if le != ri:
        print(bisect_right(dot, ri)-bisect_left(dot,le))
    else:
        if bisect_right(dot,ri) - bisect_left(dot, ri) == 1:
            print(1)
        else:
            print(0)