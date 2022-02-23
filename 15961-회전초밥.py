import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
l = []
sushi = [0 for _ in range(d+1)]
for _ in range(N):
    l.append(int(input()))

# 앞에서 k개 뽑아본다.
ans = []
tmp = 0
for i in range(k):
    if sushi[l[i]] == 0:
        tmp +=1
    sushi[l[i]] += 1
    
if sushi[c] == 0:
    tmp += 1
    ans.append(tmp)
    tmp -= 1
ans.append(tmp)

# 슬라이딩 윈도우 형식으로 한칸씩 움직인다
ptr_s = 0
ptr_e = k
while ptr_e != k-1:
    if sushi[l[ptr_e]] == 0:
        tmp += 1
    sushi[l[ptr_e]] += 1
    if sushi[l[ptr_s]] == 1:
        tmp -= 1
    sushi[l[ptr_s]] -= 1

    if sushi[c] == 0:
        tmp += 1
        ans.append(tmp)
        tmp -= 1
    ans.append(tmp)

    ptr_e += 1
    ptr_s += 1
    if ptr_e == N:
        ptr_e = 0
print(max(ans))