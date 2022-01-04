import sys
from collections import Counter
N = int(input())
list = list(map(int,sys.stdin.readline().split()))

cnt = Counter(list)
#print(cnt)
stack = []

list = [[cnt[num], int(num)] for num in list]
print(list)
answer = [-1 for _ in range(N)]
stack.append(0)

i = 1

while stack and i < N:
    while stack and list[stack[-1]][0] < list[i][0]:
        answer[stack[-1]] = list[i][1]
        stack.pop()

    stack.append(i)
    i += 1

for num in answer:
    print(num, end=' ')




'''
A = []
for i in range(len(list)):
    A.append(list.count(list[i]))

#print(A)

stack = []
ans = []
for i in range(len(A)):
    ans.append(-1)

for i in range(len(A)):
    while stack and A[i] > A[int(stack[-1])]:
        ans[stack.pop()] = list[i]

    if (not stack) or (stack and A[i] <= A[int(stack[-1])]):
        stack.append(i)


for i in range(len(ans)-1):
    print(ans[i],end=' ')
    #print(type(ans[i]))
print(ans[-1])
'''