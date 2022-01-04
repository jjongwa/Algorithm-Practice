#   ¿¬¼ÓÇÕ2
n = int(input())
arr = list(map(int,input().split()))
ansList = [[0,0] for _ in range(n)]
ansList[0] = [arr[0],0]
#print(ansList)
ans = arr[0]

for i in range(1,n):
    ansList[i][0] = max(ansList[i-1][0] + arr[i], arr[i])
    ansList[i][1] = max(ansList[i-1][0], ansList[i-1][1] + arr[i])
    ans = max(ans, ansList[i][0], ansList[i][1])
print(ans)



