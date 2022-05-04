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
dic = {}
for a in A:
    for b in B: 
        if a+b in dic:
            dic[a+b] += 1
        else:
            dic[a+b] = 1
cnt = 0
for c in C:
    for d in D:
        if -(c+d) in dic:
            cnt += dic[-(c+d)]

print(cnt)



'''
E.sort()
F.sort()

ptr_s, ptr_e = 0, len(F)-1

cnt = 0
while ptr_s != len(E)-1 or ptr_e == 0:
    if E[ptr_s] + F[ptr_e] == 0:   
        cnt += Ed[E[ptr_s]]*Fd[F[ptr_e]]
        ptr_s += 1
        ptr_e -= 1     
    elif E[ptr_s] + F[ptr_e] > 0:
        ptr_e -= 1
    elif E[ptr_s] + F[ptr_e] < 0:
        ptr_s += 1

print(cnt)
'''