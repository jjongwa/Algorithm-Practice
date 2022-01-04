S = list(input())

list = []
for i in range(26):
    list.append(chr(ord('a')+i))

ans = [-1 for _ in range(26)]

for i in range(len(S)):
    if ans[ord(S[i])-ord('a')] == -1:
        ans[ord(S[i])-ord('a')] = i

for i in ans:
    print(i,end=' ')
         


