#   Ä«À× ´Þ·Â
T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    f = 1
    while(x <= M*N):
        if x%N == y%N:
            print(x)
            f = 0
            break
        x += M
    if f:
        print(-1)


'''
for i in range(T):
    clock = [1,1]
    ans = 1
    M, N, X, Y = map(int,input().split())
    #print(M,N,x,y)
    while True:
        if clock[0] == M and clock[1] == N:
            break
        if clock[0] == X and clock[1] == Y:
            break
        clock[0] +=1
        clock[1] +=1
        ans += 1

        if clock[0] == M+1:
            clock[0] = 1
        if clock[1] == N+1:
            clock[1] = 1
    if clock[0] == M and clock[1] == N:
        print(-1)
    else:
        print(ans)
'''        