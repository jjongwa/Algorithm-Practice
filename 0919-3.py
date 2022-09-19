from itertools import combinations
N = int(input())
numList = list(map(int,input().split()))
s_num = sum(numList)
dp = [0 for _ in range(s_num+2)]

def dpdp(li, s):
    print(li, s)
    for i in li:
        if dp[i+s] == 0:            
            tmp = li.copy()
            tmp.remove(i)
            dp[i+s] = 1            
            if tmp is not None:                
                dpdp(tmp, i+s)
dpdp(numList, 0)

print(dp)