N, K = map(int, input().split())
S = list(map(int, input().split()))

ptr_s, ptr_e = 0, 0 
odd = 0
ans = 0
while ptr_e < N:
    if S[ptr_e] % 2 == 1:
        odd += 1
    ptr_e += 1
    while odd > K:
        if S[ptr_s] % 2 == 1:
            odd -= 1
        ptr_s += 1
    
    ans = max(ans, ptr_e-ptr_s-odd)
#print(ptr_s, ptr_e)
print(ans)