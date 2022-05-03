from bisect import bisect_left, bisect_right
import sys
input= sys.stdin.readline
N, M = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()
for _ in range(M):
    le, ri = map(int, input().split())
    print(bisect_right(dot, ri)-bisect_left(dot,le))