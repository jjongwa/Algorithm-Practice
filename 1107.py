#   ¸®¸ðÄÁ+
N = int(input())
M = int(input())
button = [0,1,2,3,4,5,6,7,8,9]
if M > 0:
    broken = list(map(int,input().split()))
    button = [str(x) for x in button if x not in broken]
#print(button)
else:
    button = [str(x) for x in button]


ch = 100
justMove = abs(N- ch)
ans = justMove

for i in range(1000000):
    for j in range(len(str(i))):
        if str(i)[j] not in button: 
            break
        elif len(str(i))-1 == j:
            #print(i)
            ans = min(ans, abs(N -i) + len(str(i)))
            #print(ans)
print(ans)





'''
tmp = 0
up, down = [], []
while ch != N:
    for i in range(5,-1,-1):
        target = N / (10**i)
        if target != 0:
            if target in button:
                up.append(target)
                down.append(target)
            else:
                for j in button:

'''
            
            


        
