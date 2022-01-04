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
