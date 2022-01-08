from itertools import permutations
N = int(input())
num = list(map(int,input().split()))
operators = list(map(int,input().split()))
operList = []
for i in range(len(operators)):
    for j in range(operators[i]):
        operList.append(i)

peroplList = permutations(operList, N-1)
ansList = []
for i in peroplList:
    tmp = num[0]
    for j in range(N-1):
        if i[j] == 0:
            tmp += num[j+1]
        elif i[j] == 1:
            tmp -= num[j+1]
        elif i[j] == 2:
            tmp *= num[j+1]
        elif i[j] == 3:
            if num[j+1] < 0:
                tmp = -int(tmp / (-num[j+1]))
            else:
                tmp = int(tmp / num[j+1])
        if j == N-2:
            ansList.append(tmp)

print(max(ansList))
print(min(ansList))

# pypy3 clear

# backtracking (DFS)