N, K = map(int, input().split())
numlist = list(map(int, input().split()))
count = [0 for _ in range(200001)]
ptr_s, ptr_e = 0, 0
ans = 1
count[numlist[ptr_s]] = 1

while ptr_e < N-1:
    ptr_e += 1
    count[numlist[ptr_e]] += 1
    while count[numlist[ptr_e]] > K:
        count[numlist[ptr_s]] -= 1
        ptr_s += 1
    ans = max(ans, ptr_e - ptr_s+1)
    #print(ans) 

print(ans)
'''
#시간초과 난 코드
N, K = map(int, input().split())
numlist = list(map(int, input().split()))

def countmax(arr):  # 리스트 안에 겹치는 숫자의 최댓값
    cnt = 0
    for i in arr:
        tmp = arr.count(i)
        cnt = max(cnt, tmp)

    return cnt

window = N
while window > 0:
    ptr_s = 0
    ptr_e = window
    tmplist = numlist[0:window]
    print(tmplist)
    if countmax(tmplist) <= K:
        print(window)
        exit(0)
    #print(ptr_e, N)
    while ptr_e < N:
        #print(numlist[ptr_e])
        tmplist.append(numlist[ptr_e])
        popnum = tmplist.pop(0)
        print(tmplist)
        if tmplist.count(popnum) <= K and tmplist.count(numlist[ptr_e]) <= K:
            #print(countmax(tmplist))
            print(window)
            exit(0)
        else:
            ptr_s += 1
            ptr_e += 1
    window -= 1
'''
