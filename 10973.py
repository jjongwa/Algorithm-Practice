#   이전 수열
#   다음 수열
N = int(input())
numList = [int(x) for x in input().split()]
#print(numList)

ans = -1
for i in range(len(numList)-1):
    if numList[i] > numList[i+1]:
        ans = i

if ans == -1:
    print(-1)
else:
    for j in range(ans+1, len(numList)):
        if numList[ans] > numList[j]:
            tmp = j
    
    numList[ans], numList[tmp] = numList[tmp], numList[ans]

    tmp2 = numList[ans+1:]
    tmp2.sort(reverse=True)
    ansList = numList[:ans+1] + tmp2

    for j in ansList:
        print(j, end=' ')

    