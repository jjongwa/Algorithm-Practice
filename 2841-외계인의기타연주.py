import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
N, P = map(int, input().split())
stack = [[] for _ in range(N+1)]
ans = 0
for _ in range(N):
    l, p = map(int, input().split())
    while len(stack[l]) > 0:
        #print(len(stack[l]))
        if stack[l][-1] > p:
            stack[l].pop()
            ans += 1
            #print(len(stack[l]))
        else:
            break
    if len(stack[l]) == 0 or stack[l][-1] != p:
        stack[l].append(p)
        ans += 1

print(ans)