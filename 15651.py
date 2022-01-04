#   N°ú M(3)
N, M = map(int, input().split())

stack = []
def solve():
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    for i in range(1, N+1):
        stack.append(i)
        solve()
        stack.pop()

solve()