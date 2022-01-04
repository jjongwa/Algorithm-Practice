#   가장 긴 증가하는 부분수열
N = int(input())
A = list(map(int, input().split()))
ansList = [1]* N
for i in range(1,N):
    tmp = ansList[i]
    for j in range(i-1, -1,-1):
        if A[j] < A[i] and tmp < ansList[j] + 1:
            tmp = ansList[j] + 1
    ansList[i] = tmp
        
#print(ansList)
print(max(ansList))
