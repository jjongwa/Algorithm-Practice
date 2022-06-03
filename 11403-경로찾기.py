import sys
sys.stdin = open('input.txt', 'r')

#from collections import deque
N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)] 
ans = [[0]*N for _ in range(N)] 



stack = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ans[i][j] = 1
            stack.append([i,j])
    while stack:
        start, now = stack.pop()
        for nxt in range(N):
            if ans[start][nxt] == 0 and arr[now][nxt] == 1:
                ans[start][nxt] =1
                stack.append([start, nxt])
        
for i in range(N):
    for j in range(N):
        print(ans[i][j], end=' ')
    print()