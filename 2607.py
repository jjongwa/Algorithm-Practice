N = int(input())
list = []
#print(alphabet)
for i in range(N):
    alphabet = [0 for i in range(26)]
    tmp = input()
    for j in range(len(tmp)):
        for k in range(26):
            if ord(tmp[j]) == ord('A')+k:
                alphabet[k] += 1
    list.append(alphabet)

ans = 0
'''
for i in range(N):
    print(list[i])
'''

for i in range(1, N):
    listSum = 0
    for j in range(26):
        listSum += abs(list[0][j]-list[i][j])
    if listSum <= 1:
        ans +=1
        continue
# 문자 하나 바꿨을때를 따로 검사해봐야함
    for j in range(26):
        if list[i][j] >= 1:
            list[i][j] -=1
            for k in range(26):
                if k != j:
                    list[i][k] +=1
                    if list[i] == list[0]:
                        ans+=1
                        continue
                    list[i][k] -=1
            list[i][j] +=1
print(ans)


