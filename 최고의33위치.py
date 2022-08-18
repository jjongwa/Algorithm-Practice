#N = int(input())
N = 3
arr = [[1,0,1],[0,1,0],[0,1,0]]

def count(x, y):
    global arr
    cnt = 0
    for i in range(3):
        for j in range(3):
            cnt += arr[x+i][y+j]
    print(cnt)
    return cnt

ans = count(0,0)

for i in range(N-2):
    for j in range(N-2):
        ans = max(ans, count(i,j))

print(ans)    