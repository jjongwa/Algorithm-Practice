N = int(input())
if N <100:
    print(N)
else:
    cnt = 99
    for i in range(100,N+1):
        tmp = str(i)
        if int(tmp[0]) - int(tmp[1]) == int(tmp[1]) - int(tmp[2]):
            cnt += 1
    print(cnt)