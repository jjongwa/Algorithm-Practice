# 1로 만들기
N = int(input())
ansList = [0]*1000001

for i in range(2,len(ansList)):
    tmpList = [ansList[i-1]]
    if i % 3 == 0:
        tmpList.append(ansList[int(i/3)])
    if i % 2 == 0:
        tmpList.append(ansList[int(i/2)])
    #print(tmpList)
    ansList[i] = min(tmpList) + 1
    
print(ansList[N])

'''
ans = 0
while N != 1:
    if N % 3 == 0:
        ans += 1
        N /= 3
    elif N % 2 == 0:
        ans += 1
        N /= 2
    else:
        ans += 1
        N -=1

print(ans)
'''