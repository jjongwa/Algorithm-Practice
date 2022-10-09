import copy
n, m, k = map(int, input().split())
grid = [[[] for _ in range(n)] for _ in range(n)] 

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)
def mov(x, y, atom, arr):
    m, s, d = atom[0], atom[1], atom[2]
    for _ in range(s):
        x += dx[d]
        y += dy[d]
        if x >= n:
            x %= n
        elif x < 0:            
            x += n
        if y >= n:
            y %= n
        elif y < 0:
            y += n
    arr[x][y].append([m,s,d])



# for i in range(n):
#     print(*grid[i])



for _ in range(m):
#      질량,속력,방향
    x, y, m, s, d = map(int, input().split())
    grid[x-1][y-1].append([m, s, d])

# for i in range(n):
#     print(*grid[i])

for _ in range(k):
    ans = 0
    tmp = [[[] for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) != 0:
                for l in range(len(grid[i][j])):
                    # print(i, j ,l)
                    mov(i, j, grid[i][j][l], tmp)
                while grid[i][j]:
                    grid[i][j].pop()

    for i in range(n):
        for j in range(n):
            if len(tmp[i][j]) > 1:
                nm, ns, nd = 0, 0, []
                for l in range(len(tmp[i][j])):
                    nm += tmp[i][j][l][0]
                    ns += tmp[i][j][l][1]
                    nd.append(tmp[i][j][l][2])
                nm = nm//5
                ns = ns // len(tmp[i][j])
                while tmp[i][j]:
                    tmp[i][j].pop()
                if nm == 0:
                    continue
                else:
                    dire = 0
                    for ndd in nd:
                        dire += (ndd%2)
                    if dire == 0 or dire == len(nd):
                        for mm in range(4):
                            tmp[i][j].append([nm, ns, mm*2])
                    else:
                        for mm in range(4):
                            tmp[i][j].append([nm, ns, mm*2+1])
                    
    for i in range(n):
        for j in range(n):
            if len(tmp[i][j]) > 0:
                for l in range(len(tmp[i][j])):
                    ans += tmp[i][j][l][0]


    grid = copy.deepcopy(tmp)



    # print()
    # for i in range(n):
    #     print(*grid[i])
    
print(ans)
