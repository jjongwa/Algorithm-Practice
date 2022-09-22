n = int(input())
ans = 0
numList = [n]
while True:
    if n % 2 == 0:
        n = n//2
    else:
        n = n*3 -1

    if n in numList:
        print(-1)
        break
    numList.append(n)

    ans += 1
    
    if n == 1:
        print(ans)
        break
