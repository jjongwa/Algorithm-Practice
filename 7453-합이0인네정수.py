import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    tmpinput = list(map(int, input().split()))
    A.append(tmpinput[0])
    B.append(tmpinput[1])
    C.append(tmpinput[2])
    D.append(tmpinput[3])
#print(A,B,C,D)

E, F = {}, {}
'''
for i in range(n):
    for j in range(n):
        if not E.get(A[i]+B[j]):
            E[A[i]+B[j]] = 1
        else:
            E[A[i]+B[j]] += 1
        if not F.get(C[i]+ D[j]):
            F[C[i]+ D[j]] = 1
        else:
            F[C[i]+ D[j]] += 1
'''

for i in A:
    for j in B:
        if not E.get(i+j):
            E[i+j] = 1
        else:
            E[i+j] += 1

for i in C:
    for j in D:
        if not F.get(i+j):
            F[i+j] = 1
        else:
            F[i+j] += 1


ans = 0

for _, key in enumerate(E):
    if F.get(-key):
        ans += E[key]* F[-key] 

print(ans)

'''
ptr_s, ptr_e = 0, n*n -1
E.sort()
F.sort()

while ptr_s != n*n and ptr_e != -1:
    if E[ptr_s] + F[ptr_e] == 0:
        ans += 1
        ptr_s += 1
        
    elif E[ptr_s] + F[ptr_e] > 0:
        ptr_e -= 1
    elif E[ptr_s] + F[ptr_e] < 0:
        ptr_s += 1

'''








'''
시간초과 뜬다..!
반반 나눠서 합친 후 시도해보아야 할듯
import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    tmpinput = list(map(int, input().split()))
    A.append(tmpinput[0])
    B.append(tmpinput[1])
    C.append(tmpinput[2])
    D.append(tmpinput[3])
#print(A,B,C,D)
ptr_a, ptr_b, ptr_c, ptr_d = 0,0,0,0

nowSum = A[ptr_a] + B[ptr_b] + C[ptr_c] + D[ptr_d]
ans = 0
if nowSum == 0:
    ans += 1

while ptr_d != n:
    nowSum -= A[ptr_a]
    ptr_a += 1
    if ptr_a == n: # a가 0으로 
        ptr_a = 0
        nowSum += A[ptr_a]
        nowSum -= B[ptr_b]
        ptr_b += 1
        if ptr_b == n: # b가 0으로
            ptr_b = 0
            nowSum += B[ptr_b]
            nowSum -= C[ptr_c]
            ptr_c += 1
            if ptr_c == n: # c가 0으로
                ptr_c = 0
                nowSum += C[ptr_c]
                nowSum -= D[ptr_d]
                ptr_d += 1
                if ptr_d <n:
                    nowSum += D[ptr_d]
            else:
                nowSum += C[ptr_c]
        else:
            nowSum += B[ptr_b]
    else:
        nowSum += A[ptr_a]

    if nowSum == 0:
        #print(A[ptr_a], B[ptr_b],C[ptr_c], D[ptr_d])
        ans += 1

print(ans)


'''
