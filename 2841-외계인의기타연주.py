import sys
sys.stdin = open('input.txt', 'r')

N, P = map(int, input().split())
stack = [[] for _ in range(N+1)]
ans = 0
for _ in range(N):
    l, f = map(int, input().split())
    while len(stack[l]) > 0:
        #print(len(stack[l]))
        if stack[l][len(stack[l])-1] > f:
            stack[l].pop()
            ans += 1
            #print(len(stack[l]))
        else:
            break
    if len(stack[l]) == 0 or stack[l][len(stack[l])-1] != f:
        stack[l].append(f)
        ans += 1

print(ans)