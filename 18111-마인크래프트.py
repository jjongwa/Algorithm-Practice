import sys
sys.stdin = open('input.txt', 'r')
input  = sys.stdin.readline
N, M, B = map(int, input().split())
hi = 0
lo = 256
filed = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    hi = max(hi, max(tmp))
    lo = min(lo, min(tmp)) 
    filed.append(tmp)

ans = 256*500*500*2
ansList = []
tt = 0
for i in range(lo,hi+1):
    iv = B
    cnt = 0
    for x in range(N):
        for y in range(M):
            if filed[x][y] > i:
                tmp = filed[x][y] - i
                iv +=  tmp
                cnt += 2*tmp
            elif filed[x][y] < i:
                tmp = i - filed[x][y]
                iv -= tmp
                cnt += tmp
            tt += 1
    if iv < 0:
        continue
    if ans >= cnt:
        #print(ans, cnt)
        ans = cnt
        ansList.append((ans, i))
#print(ansList)
print(ansList[len(ansList)-1][0], ansList[len(ansList)-1][1])


print(tt)