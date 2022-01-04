#   가장 큰 증가 부분 수열

N = int(input())
A = list(map(int,input().split()))

ansList  = [0 for _ in range(N)]
ansList[0] = A[0]
for i in range(1,N):
    tmp = []
    for j in range(i):
        if A[i] > A[j]:
            tmp.append(ansList[j])
    if not tmp:
        ansList[i] = A[i]
    else:
        ansList[i] = A[i] + max(tmp)
#    print(ansList)

print(max(ansList))