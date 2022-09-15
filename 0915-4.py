n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def Squre(st_a,st_b, a, b):
    ans = 0
    for i in range(a):
        for j in range(b):
            ans += grid[st_a+i][st_b+j]
    return ans
compare = 0

for i in range(n):
    for j in range(n):
        for k in range(n+1):
            for l in range(n+1):
                if i+k<=n and j+l<=n:
                    compare = max(compare,Squre(i,j,k,l))
                    #print(compare, i, j, k ,l)
print(compare)