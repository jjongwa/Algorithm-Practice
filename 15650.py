#   N°ú M (2)

N, M = map(int, input().split())

stack = []
def solve(x):
    if len(stack) == M:
        stack.sort()
        print(' '.join(map(str,stack)))
        return
    for i in range(x, N+1):
        if i in stack:
            continue
        stack.append(i)
        solve(i+1)
        stack.pop()

solve(1)
