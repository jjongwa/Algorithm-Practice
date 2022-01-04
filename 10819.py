#   차이를 최대로
N = int(input())
A = list(map(int,input().split()))

stack = []
ansList = []
def swap():
    if len(stack) == N:
        tmp = [A[x-1] for x in stack]
        #print(stack)
        ansList.append(tmp)
        return
    for i in range(1, N+1):
        if i in stack:
            continue
        stack.append(i)
        swap()
        stack.pop()

swap()

#print(ansList)


ans = 0
for arr in ansList:
    tmp = 0
    for j in range(N-1):
        tmp += abs(arr[j] - arr[j+1])

    ans = max(ans, tmp)

print(ans)
