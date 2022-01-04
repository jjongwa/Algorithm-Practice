S = list(input())

list = []
for i in range(26):
    list.append(chr(ord('a')+i))
ans = []
for i in list:
    print(S.count(i),end=' ')


