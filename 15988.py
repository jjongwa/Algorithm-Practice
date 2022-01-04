#   1,2,3 ´õÇÏ±â 3
ansList = [0,1,2,4] +[0]*999997
for i in range(4,len(ansList)):
    ansList[i] = ansList[i-1] %1000000009 + ansList[i-2] %1000000009 + ansList[i-3] %1000000009
    
T  = int(input())
for i in range(T):
    n = int(input())
    print(ansList[n]%1000000009)

