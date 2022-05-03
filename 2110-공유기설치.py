import sys
input = sys.stdin.readline
N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])
#print(house)
lo = min(house)
hi = max(house)
mid = (hi-lo) // C
lo = 1

def is_possible(mid):
    cnt = C-2
    last = 0
    if cnt == 0:
        print(max(house)- min(house))
        exit(0)
    for i in range(1, N-1):
        if house[i] - house[last] >= mid:
            #print('i=', i)
            #print('house[i] = ',house[i], 'house[last] = ',house[last])
            last  = i
            cnt -= 1
            #print(cnt)
            if cnt == 0 and house[N-1] - house[i] < mid:
                #print(house[N-1],house[i],house[N-1] - house[i], 'F1')
                return False

    if cnt > 0:
        #print('F2')
        return False
    else:
        #print('T')
        return True

ans = 0
while lo <= hi:
    #print(lo, hi, mid)
    if is_possible(mid):
        lo = mid+1
        ans = mid
        #print(ans)
    else:
        hi = mid -1
    mid = (lo + hi) // 2
print(ans)