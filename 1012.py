import sys
sys.setrecursionlimit(10000)

# recursionerror

T = int(input())    # test case #
for j in range(T):
    M, N, K = map(int,input().split())  # row, col, # of 1
    farm = [[0]*M for _ in range(N)]
    count = 0

    def find(y, x):
        if farm[y][x] ==1:
            farm[y][x] = 0
        else:
            return

        if y > 0:
            find(y-1,x)
        if y < N-1:
            find(y+1,x)
        if x > 0:
            find(y,x-1)
        if x <M-1:
            find(y, x+1)

    for i in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1
        
    for i in range(N):
        for k in range(M):
            if farm[i][k] == 1:
                count +=1
                find(i,k)
                farm[i][k] = 0
                #print(farm)

    print(count)
    

