#   N°ú M(7)
N, M = map(int, input().split())
numList = list(map(int,input().split()))
numList.sort()
stack = []
def solve():
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    for i in numList:
        stack.append(i)
        solve()
        stack.pop()

solve()
