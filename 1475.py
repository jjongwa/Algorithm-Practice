n = int(input())
nList = [0] * 10
while True:
    nowNum = n % 10
    n = n // 10
    nList[nowNum] += 1
    if n == 0:
        break
sixOrNine = nList[6] + nList[9]

if sixOrNine % 2 == 1:
    nList[6] = sixOrNine // 2 + 1
    nList[9] = sixOrNine // 2 + 1
else:
    nList[6] = sixOrNine // 2
    nList[9] = sixOrNine // 2

print(max(nList))
