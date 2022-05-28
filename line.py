answer = 0
fuel =19
powers = [40, 30, 20, 10]
distances = [1000, 2000, 3000, 4000]


def cal(f, p, dis):
    if f*p*f/2 >dis:
        time = (dis * 2/ p) **(1/2)
    else:
        time = (dis - f*p*f/2) /(p*f) + f
    
    if time != time//1:
        time = time//1 + 1
    else:
        time = time // 1
    return time


fuel -= len(powers)
flist = [1] * len(powers)
ntime = [0] * len(powers)
for i in range(len(powers)):
    ntime[i] = cal(flist[i], powers[i], distances[i])

while fuel:
    tmp = 0
    for i in range(len(powers)):
        if cal(flist[i], powers[i], distances[i])  >= tmp:
            tmp = cal(flist[i], powers[i], distances[i]) 
            nxtf = i
    flist[nxtf] += 1
    ntime[nxtf] = int(cal(flist[nxtf]+1, powers[nxtf], distances[nxtf]))
    fuel -= 1    
tmp2 = 0
ans = 0
for i in range(len(flist)):
    if tmp2 < flist[i]:
        tmp2 = flist[i]
        ans = i
answer = int(cal(flist[ans], powers[ans], distances[ans]))
print(answer)













'''
n = 5
times = [2, 4, 5]

answer = 0
dp = [0] * (n+1)
dp[2] = times[0]

if n == 2:
    answer = dp[2]
else:
    for i in range(3, n+1):
        tmp  = []
        for j in range(1, i//2+1):
            tmp.append(dp[i-j] + times[j-1])
        dp[i] = min(tmp)
    answer = dp[n]
print(answer)

'''
