#   가장 긴 감소하는 부분 수열
N = int(input())
A = list(map(int,input().split()))

ansList  = [1 for _ in range(N)]

for i in range(1,N):
    tmp = []
    for j in range(i):
        if A[i] < A[j]:
            tmp.append(ansList[j])
    if tmp:
        ansList[i] += max(tmp)
    print(ansList)

print(max(ansList))