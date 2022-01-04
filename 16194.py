#   카드 구매하기2
N = int(input())
P = [0] + list(map(int, input().split()))
ansList = [0,P[1]] + [0]* (N-1)
ansList[2] = min(P[2], P[1]*2)

for i in range(3,N+1):
    ansList[i] = P[i]
    for j in range(1,int(i/2)+1):
        ansList[i] = min(ansList[i], ansList[j] + ansList[i-j])

print(ansList[N])
