# 1,2,3 ´õÇÏ±â
ansList = [0,1,2,4] +[0]*8
for i in range(4,len(ansList)):
    ansList[i] = ansList[i-1] + ansList[i-2] + ansList[i-3]
    
T  = int(input())
for i in range(T):
    n = int(input())
    print(ansList[n])

