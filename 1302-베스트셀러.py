import sys
dic = dict()
for _ in range(int(input())):
    bookname = input()
    if bookname in dic:
        dic[bookname] += 1
    else:
        dic[bookname] = 1
m = max(dic.values())   # 딕셔너리의 value 중 최댓값
ansList = []

for i in dic:
    if dic[i] == m:
        ansList.append(i)
        
print(sorted(ansList)[0])


'''
dic = {}
for _ in range(int(input())):
    bookName = input()
    if bookName in dic:
        dic[bookName] += 1
    else:
        dic[bookName] = 1
#print(dic)
sorted_dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)
#print(sorted_dic)
count =sorted_dic[0][1] 
ans = []
for i in sorted_dic:
    if i[1] == count:
        ans.append(i[0])
ans.sort()
#print(ans)
print(ans[0])
'''





