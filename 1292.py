A, B = map(int,input().split())

list = []

for i in range(1000):
    for j in range(i):
        list.append(i)

ans = 0
for i in range(A-1,B,1):
    ans += list[i]

print(ans)
