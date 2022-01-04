#   모든 순열
N = int(input())
#numList = [int(x+1) for x in range(N)]
stack = []
def solve():
    if len(stack) == N:
        print(' '.join(map(str,stack)))
        return
    for i in range(1, N+1):
        if i in stack:
            continue
        stack.append(i)
        solve()
        stack.pop()

solve()
