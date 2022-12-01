import sys
input = sys.stdin.readline
n, k = map(int,input().split())
nList = list(map(int, input().split()))

dic = {}
for i in nList:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = -1
for i in dic:
    if dic[i] < k:
        continue
    if ans < i:        
        ans = i
print(ans)