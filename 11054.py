#   가장 긴 바이토닉 부분 수열

N = int(input())
A = list(map(int,input().split()))

ansList1  = [1 for _ in range(N)]
ansList2  = [1 for _ in range(N)]

for i in range(1,N):
    tmp = []
    for j in range(i):
        if A[i] > A[j]:
            tmp.append(ansList1[j])
    if tmp:
        ansList1[i] += max(tmp)
print(ansList1)


for i in range(N-1,-1,-1):
    tmp = []
    for j in range(N-1,i,-1):
        if A[i] > A[j]:
            tmp.append(ansList2[j])
    if tmp:
        ansList2[i] += max(tmp)

ansList = []
for i in range(N):
    ansList.append(ansList1[i] + ansList2[i])
print(ansList2)
print(max(ansList)-1)