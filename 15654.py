#   N°ú M (5)
N, M = map(int, input().split())
numList = list(map(int,input().split()))
numList.sort()
stack = []
def solve():
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    for i in numList:
        if i in stack:
            continue
        stack.append(i)
        solve()
        stack.pop()

solve()
