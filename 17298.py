import sys
N = int(input())
A = sys.stdin.readline().split()

stack = []
ans = []
for i in range(len(A)):
    ans.append(-1)

for i in range(len(A)):
    while stack and int(A[i]) > int(A[int(stack[-1])]):
        ans[stack.pop()] = int(A[i])

    if (not stack) or (stack and int(A[i]) <= int(A[int(stack[-1])])):
        stack.append(i)


for i in range(len(ans)-1):
    print(ans[i],end=' ')
    #print(type(ans[i]))
print(ans[-1])












'''
print(A[2], A[10])
if A[2] < A[10]:
    print('wow')
if 999999 < 1000000:
    print('wow2')
'''

'''
for i in range(len(A)):
    tri = 0
    if i != len(A)-1:
        for j in range(i+1,len(A),1):
            #print(A[j])
            if A[i] == '1000000':
                break
            elif int(A[j]) > int(A[i]) or A[j] == '1000000':
                print(A[j],end='')
                tri = 1
                break

    if tri == 0:
        print(-1,end='')
    if i != len(A)-1:
        print(' ',end='')
'''