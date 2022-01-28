# 서울 지하철 2호선
import sys
from collections import deque
sys.setrecursionlimit(10**9)

N = int(input())
check = [0] * (N+1)
dist = [0] * (N+1)

def dfs(x, cnt):
    if check[x] == 1:
        if cnt - dist[x] >= 3:
            return x
        else:
            return -1
    check[x] = 1
    dist[x] = cnt

    




graph = [[] for _ in range(N+1)]
graphsize = [0] * (N+1)
for _ in range(N):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    graphsize[A] += 1
    graphsize[B] += 1

while 1 in graphsize:
    for i in range(1, N+1):
        if graphsize[i] == 1:



# https://vixxcode.tistory.com/25 참고