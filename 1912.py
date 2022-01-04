#   ¿¬¼ÓÇÕ
n = int(input())
mem = list(map(int,input().split()))
memList = [0] * n


for i in range(n):
    '''
    if i ==0:
        print(memList[-1])
    '''
    memList[i] = max(memList[i-1]+mem[i] , mem[i])
     
memList.append(-1001)
print(max(memList))