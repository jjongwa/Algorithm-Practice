# 소수 구하기
list = [0]*1000001
list[1] = 1
for i in range(2,1000001,1):
    if list[i] == 0:
        for j in range(i*2,1000001,i): 
            list[j] = 1

M, N = map(int, input().split())

for i in range(M,N+1,1):
    if list[i] == 0:
        print(i)




'''
for i in range(M,N+1,1):
    tri = 0
    if i == 1:
        continue
    for j in range(2,i,1):
        if i % j == 0:
            tri = 1
            break;
    if tri == 0:
        print(i)
'''





'''
#소수 찾기
N = int(input())
list = list(map(int,input().split()))
ans = len(list)
for i in list:
    if i == 1:
        ans -=1
        continue
    for j in range(2,i,1):
        if i % j == 0:
            ans -= 1
            break;

print(ans)
'''