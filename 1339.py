N = int(input())
alphabet = [0]*26
for _ in range(N):
    alpa = list(input().rstrip())
    for i in range(len(alpa)):
        alphabet[ord(alpa[i])- 65] += 10 ** (len(alpa)-i-1)
alphabet.sort(reverse=True)
#print(alphabet)
num = 9
ans = 0
for i in range(len(alphabet)):
    ans += num*alphabet[i]
    num -=1

print(ans)


'''
import itertools
N = int(input())
alpa = []
for i in range(N):
    tmp = input()
    al_num = ''
    for j in range(len(tmp)):
        al_num += str(ord(tmp[j]) - 65)
            
    alpa.append(al_num)

#print(alpa)
numList = [i for i in range(10)]
numList = list(itertools.permutations(numList,10))
#print(numList)
ans = []
for k in range(len(numList)):
    anssum = 0
    anstmp = ''
    for i in range(N):
        for j in range(len(alpa[i])):
            #print(numList[k][int(alpa[i][j])])
            anstmp += str(numList[k][int(alpa[i][j])])

        anssum += int(anstmp)
    print(anssum)
    ans.append(anssum)

#print(max(ans))
'''