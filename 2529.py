import itertools
k = int(input())
oper = list(map(str,input().split()))
numList = [x for x in range(10)]
ansList = list(itertools.permutations(numList,k+1))
ansList.sort()
ans = []
#print(k)
#print(ansList[len(ansList)-1][k])
for i in range(len(ansList)):
    for j in range(k):
        #print(int(ansList[i][j]), ansList[i][j])
        #print(k)
        if oper[j] == '>' and int(ansList[i][j]) > int(ansList[i][j+1]):
            continue
        elif oper[j] == '<' and ansList[i][j] < ansList[i][j+1]:
            continue
        else:
            break
    else:
        tmp = ''
        for ii in ansList[i]:
            tmp += str(ii)
        ans.append(tmp)
        break

for i in range(len(ansList)-1,-1,-1):
    for j in range(k-1,-1,-1):
        #print(int(ansList[i][j]), ansList[i][j])
        #print(k)
        if oper[j] == '>' and int(ansList[i][j]) > int(ansList[i][j+1]):
            continue
        elif oper[j] == '<' and ansList[i][j] < ansList[i][j+1]:
            continue
        else:
            break
    else:
        tmp = ''
        for ii in ansList[i]:
            tmp += str(ii)
        ans.append(tmp)
        break





print(max(ans))
print(min(ans))

# 다 찾지말고 앞뒤에서 하나씩 찾기