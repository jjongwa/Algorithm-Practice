N = int(input())
l = list(map(int, input().split()))
ptr_s, ptr_e = 0, N-1
ans = 2000000000
l.sort()
#print(l)
while ptr_s != ptr_e:
    tmp = l[ptr_s] + l[ptr_e]
    #print(tmp)
    if tmp == 0:
        print(l[ptr_s], l[ptr_e])
        exit(0)
    if abs(tmp) < ans:
        ans = abs(tmp)
        ans_s, ans_e = ptr_s, ptr_e
    if tmp < 0:
        ptr_s += 1
    elif tmp > 0:
        ptr_e -= 1
#print(l)
#print(ans_s, ans_e)
print(l[ans_s], l[ans_e])


