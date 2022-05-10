N = int(int(input()))

def incline(a,b):
    return (bd[b] - bd[a]) / abs((b-a))
bd = list(map(int, input().split()))
le, ri = 0, 0
ansList = [0 for _ in range(N)]
for i in range(N):
    cnt = 0
    #print("i =", i)
    if i != 0:
        cnt += 1
        le = incline(i, i-1)
        #print("le는",le)
        if i > 1:
            for j in range(i-2, -1,-1):            
                if le >= 0:
                    if bd[i]+le*(i-j) < bd[j]:
                        cnt += 1
                        le = incline(i, j)
                else:
                    if bd[i]+le*(i-j) < bd[j]:
                        cnt += 1
                        le = incline(i, j)
    if i != N-1:
        cnt += 1
        ri = incline(i,i+1)
        #print("ri는",ri)
        if i < N-2:
            for j in range(i+2, N):
                if ri >= 0:
                    if bd[i]+ri*(j-i) < bd[j]:
                        cnt += 1
                        ri = incline(i, j)
                else:
                    if bd[i]+ri*(j-i) < bd[j]:
                        cnt += 1
                        ri = incline(i, j)
    ansList[i] = cnt
#print(ansList)
print(max(ansList))
    
