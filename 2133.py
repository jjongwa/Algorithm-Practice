#   타일 채우기
N = int(input())

ansList = [0 for _ in range(N+1)]
#ansList[0] = 1
if N>=2:
    ansList[2] = 3
for i in range(4,N+1):
    if i%2 == 0:
        ansList[i] = ansList[i-2]*3 + sum(ansList[:i-2])*2 +2
    
    
#print(ansList)
print(ansList[N])




# N이  1일떄!!!!!!!!!!!!!!!!!