import sys
import copy
INT_MAX = sys.maxsize
N, M = map(int, input().split())
coin = list(map(int, input().split()))
coin.sort()
dp = [INT_MAX] * (M+1)

def pick(num, c, last):
    if c > M:
        return

    for i in range(N):
        if c+coin[i] > M or i in last:
            continue
        tmp = copy.deepcopy(last)
        
        if dp[c+coin[i]] == INT_MAX:
            dp[c+coin[i]] = num+1
            tmp.append(i)
            pick(num+1, c+coin[i], tmp) 
        else:
            if num+1 < dp[c+coin[i]]:
                tmp.append(i)
                dp[c+coin[i]] = num + 1
                pick(num+1, c+coin[i], tmp)
            else:
                pick(num, c+coin[i],tmp)        

        if c+ coin[i] == M:
            print(tmp)
pick(0,0,[])
print(dp)