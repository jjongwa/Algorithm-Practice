import sys
sys.setrecursionlimit(10**6)

W, H = map(int,input().split())
field = [[0 for _ in range(H+2)]for _ in range(W+2)]
visited = [[0 for _ in range(H+2)]for _ in range(W+2)]
for i in range(1,H+1):
    tmp = list(input().split())
    for j in range(1,W+1):
        field[j][i] += int(tmp[j-1])

def see(arr):
    for i in range(1,H+1):
        for j in range(1,W+1):
            print(arr[j][i],end=' ')
        print()

#see(field)

stack = []
#stack.append([0,0])
cnt = 0

def dfs(x,y,arr):
    global cnt
    '''
    if visited[x][y] == 1:
        return
    '''

    visited[x][y] = 1

    if y%2 == 0:
        if x-1 >= 0 and y-1 >= 0 and arr[x-1][y-1] == 1:
            cnt+=1
        elif x-1 >= 0 and y-1 >= 0 and visited[x-1][y-1] == 0:
            stack.append([x-1, y-1])
            visited[x-1][y-1] = 1
        if x-1 >= 0 and arr[x-1][y] == 1:
            cnt+=1
        elif x-1 >= 0 and visited[x-1][y] == 0:
            stack.append([x-1, y])
            visited[x-1][y] = 1
        if x-1 >= 0 and y+1 <= H+1 and arr[x-1][y+1] == 1:
            cnt+=1
        elif x-1 >= 0 and y+1 <= H+1 and visited[x-1][y+1] == 0:
            stack.append([x-1, y+1])
            visited[x-1][y+1] = 1
        if y+1 <= H+1 and arr[x][y+1] == 1:
            cnt+=1
        elif y+1 <= H+1 and visited[x][y+1] == 0:
            stack.append([x,y+1])
            visited[x][y+1] = 1
        if x+1 <= W+1 and arr[x+1][y] == 1:
            cnt+=1
        elif x+1 <= W+1 and visited[x+1][y] == 0:
            stack.append([x+1,y])
            visited[x+1][y] = 1
        if y-1 >= 0 and arr[x][y-1] == 1:
            cnt+=1
        elif y-1 >= 0 and visited[x][y-1] == 0:
            stack.append([x,y-1])
            visited[x][y-1] = 1
    else:
        if y-1 >= 0 and arr[x][y-1] == 1:
            cnt+=1
        elif y-1 >= 0 and visited[x][y-1] == 0:
            stack.append([x,y-1])
            visited[x][y-1] = 1
        if x-1 >= 0 and arr[x-1][y] == 1:
            cnt+=1
        elif x-1 >= 0 and visited[x-1][y] == 0:
            stack.append([x-1,y])
            visited[x-1][y] = 1
        if y+1 <= H+1 and arr[x][y+1] == 1:
            cnt+=1
        elif y+1 <= H+1 and visited[x][y+1] == 0:
            stack.append([x,y+1])
            visited[x][y+1] = 1
        if x+1 <= W+1 and y+1 <= H+1 and arr[x+1][y+1] == 1:
            cnt+=1
        elif x+1 <= W+1 and y+1 <= H+1 and visited[x+1][y+1] == 0: 
            stack.append([x+1,y+1])
            visited[x+1][y+1] = 1
        if x+1 <=W+1 and arr[x+1][y] == 1:
            cnt+=1
        elif x+1 <=W+1 and visited[x+1][y] == 0:
            stack.append([x+1,y])
            visited[x+1][y] = 1
        if x+1 <= W+1 and y-1 >= 0 and arr[x+1][y-1] == 1:
            cnt+=1
        elif x+1 <= W+1 and y-1 >= 0 and visited[x+1][y-1] == 0:
            stack.append([x+1,y-1])
            visited[x+1][y-1] = 1
    
    if not stack:
        return
    #print(stack, cnt)
    n = stack.pop()
    dfs(n[0],n[1],arr)

dfs(0,0,field)

print(cnt)

# recursion error 뜨니까 sys로 재귀 깊이 조정
# 문제 잘 보고 구현하자