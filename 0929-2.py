n, m , k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)

ap, bp = 0,0
ans = 0
while ap < n and bp < m:
    # print(ap,bp,A[ap], B[bp], ans)
    if A[ap] + B[bp] == k:
        ans += 1
        ap += 1
        bp += 1
    elif A[ap] + B[bp] > k:
        bp += 1
    elif A[ap] + B[bp] < k:
        ap += 1
    

print(ans)