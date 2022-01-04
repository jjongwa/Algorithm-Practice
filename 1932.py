#   Á¤¼ö »ï°¢Çü 
n = int(input())
triList = []
for i in range(n):
    triList.append(list(map(int,input().split())))

for i  in  range(1,n):
    for j in range(i+1):
        #print(j)
        if j == 0:
            triList[i][j] += triList[i-1][j]
        elif j == i:
            triList[i][j] += triList[i-1][j-1]
        else:
            triList[i][j] += max(triList[i-1][j-1], triList[i-1][j])

print(triList)
print(max(triList[n-1]))