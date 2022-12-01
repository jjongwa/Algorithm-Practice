n = int(input())
numList = list(map(int, input().split()))
od, ev = [], []
for n in numList:
    if n % 2 == 0:
        ev.append(n)
    else:
        od.append(n)

ev.sort()
od.sort(reverse=True)


for i in range(len(od)):
    print(ev[i], od[i], end=" ")

