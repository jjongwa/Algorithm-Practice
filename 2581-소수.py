num = [0 for _ in range(10001)]
num[1] = 1
for i in range(2, 10001):
    for j in range(2*i, 10001, i):
        if num[j] == 0:
            num[j] = 1

M = int(input())
N = int(input())

minNum = -1
ans = 0
for i in range(M, N+1):
    if num[i] == 0:
        if minNum == -1:
            minNum = i
        ans += i

if minNum == -1:
    print(minNum)
else:
    print(ans, minNum)