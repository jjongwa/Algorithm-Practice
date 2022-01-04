#   Base Conversion
A, B = map(int, input().split())
m = int(input())
future = list(map(int, input().split()))
ten = 0
for i in range(m):
    ten += A**(m-i-1)*future[i]
#print(ten)
ans = []
while ten!= 0:
    ans.append(ten%B)
    ten //= B

for i in reversed(ans):
    print(i,end=' ')