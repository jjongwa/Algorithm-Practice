# N°ú M (1)
N, M = map(int, input().split())

stack = []
def solve():
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    for i in range(1, N+1):
        if i in stack:
            continue
        stack.append(i)
        solve()
        stack.pop()

solve()



'''
numberList = [ x+1 for x in range(M)]
#print(numberList)

for i in range(N):
'''