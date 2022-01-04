# 퐁당퐁당2
N = int(input())
P, T  = map(int,input().split())

def skip(n, r):
    sum = 0;
    for i in range(1,r):
        if i >n*2:
            sum += n*4 - i
        else:
            sum +=i
    return sum

def play(n,p,t):
    round = int((n*n*4 - 1) % (n*2))
    roundT = n*4 -2

    remain = t % roundT
    hand = (round*int(t/roundT) + skip(n,remain)) % (n*2)
    start = 0

    if remain > n*2:
        start += n*4 - remain
    else:
        start += remain

    for i in range(start):
        hand += 1
        if hand > n*2:
            hand %= (n*2)
        if hand == (p*2 -1) or hand == p*2:
            return 1
    return 0

#print(play(N,P,T))
if play(N,P,T):
    print("Dehet YeonJwaJe ^~^")
else:
    print("Hing...NoJam")    















'''
T = T % (4*N -1)
count = 0
start = 1
arr = []
for i in range(1,T+1):
    size = i
    if i > N*2:
        size = N*4 - i
    for j in range(1,size+1):    
        if i == T:
            arr.append(start)    
        count += 1
        if count ==2:
            start += 1
            count = 0

if P in arr:
    print("Dehet YeonJwaJe ^~^")
else:
    print("Hing...NoJam")

'''