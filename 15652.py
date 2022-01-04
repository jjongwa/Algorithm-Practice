#   N°ú M (4)

N, M = map(int, input().split())

stack = []
def solve(x):
    if len(stack) == M:
        stack.sort()
        print(' '.join(map(str,stack)))
        return
    for i in range(x, N+1):
        stack.append(i)
        solve(i)
        stack.pop()

solve(1)