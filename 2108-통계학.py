import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr =[]
cnt = {}
for _ in range(N):
    n = int(input())
    arr.append(n)
    if n not in cnt:
        cnt[n] = 1
    else:
        cnt[n] += 1
k = 0
ans = []
for i in cnt:
    if k < cnt[i]:
        k = cnt[i]
        ans = []
        ans.append(i)
    elif k == cnt[i]:
        ans.append(i)
ans.sort()
arr.sort()

print(round(sum(arr)/N))
print(arr[N//2])
if len(ans) >1:
    print(ans[1])
else:
    print(ans[0])
print(max(arr) - min(arr))