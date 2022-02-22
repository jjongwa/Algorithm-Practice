N, X = map(int, input().split())
days = list(map(int, input().split()))

pt_s = 0
ans = sum(days[:X])
count = 1
tmpsum = ans
for pt_e in range(X, N):
    tmpsum += days[pt_e]
    tmpsum -= days[pt_s]
    if ans == tmpsum:
        count +=1
    elif ans < tmpsum:
        ans = tmpsum
        count = 1
    pt_s +=1

if ans == 0:
    print('SAD')
else: 
    print(ans)
    print(count)


#tmpsum을 계속 바꾸어야 한다


'''
N, X = map(int, input().split())
days = list(map(int, input().split()))

pt_s = 0
pt_e = X-1
ans = 0
count = 0
while pt_e < N:
    if ans == sum(days[pt_s:])- sum(days[pt_e+1:]):
        count +=1
    else:
        ans = max(ans, sum(days[pt_s:])- sum(days[pt_e+1:]))
        count = 1
    pt_s +=1
    pt_e +=1

if ans == 0:
    print('SAD')
else: 
    print(ans)
    print(count)
'''