#   진법 변환2
dic ={10:'A'}
for i in range(11,36,1):
    dic[i] = chr(ord('A')+i-10)

N, B = map(int, input().split())
ans = []
while N > 0:
    if N%B >9:
        ans.append(dic[N%B])
    else:
        ans.append(str(N%B))
    N = N//B

print(''.join(reversed(ans)))