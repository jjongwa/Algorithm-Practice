# 가장 긴 증가하는 부분수열 4
N = int(input())
A = list(map(int, input().split()))
ansList = [1]* N
ansMem = [[] for _ in range(N)]

for i in range(N):
    ansMem[i].append(A[i])
#print(ansMem)

for i in range(1,N):
    tmp = ansList[i]
    for j in range(i-1, -1,-1):
        if A[j] < A[i] and tmp < ansList[j] + 1:
            tmp = ansList[j] + 1
            ansMem[i] = ansMem[j] + [A[i]]
    ansList[i] = tmp

ansA, ansB = 0,0
for i in range(N):
    if ansA < ansList[i]:
        ansB = i
        ansA = ansList[i]
print(ansA)
print(*ansMem[ansB])

'''
for i in range(1,N):
    tmp = ansList[i]
    t = 0
    for j in range(i-1, -1,-1):
        if A[j] < A[i] and tmp < ansList[j] + 1:
            tmp = ansList[j] + 1
            t = j
    ansList[i] = tmp
    #print(ansMem[i], ansMem[t])
    ansMem[i] = ansMem[i] +ansMem[t]
    #ansMem[i].append(A[i])
    
#print(ansMem)
#print(ansList)
ansA, ansB = 0,0
for i in range(len(ansList)):
    if ansA < ansList[i]:
        ansA = ansList[i]
        ansB = i
print(ansA)
for i in range(len(ansMem[ansB])-1,-1,-1):
    print(ansMem[ansB][i],end=' ')
#print(ansMem[ansB])
'''