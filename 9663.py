# N-Queen
N = int(input())

ans = 0
queenList = [0 for _ in range(N)]  
def N_Queen(now, end):
    global ans
    if now == end:
        print(queenList)
        ans+=1
        return
    else:
        for i in range(N):
            queenList[now] = i
            for j in range(now):
                if queenList[j] == queenList[now]:
                    break
                if abs(queenList[j]-queenList[now]) == now- j:
                    break
            else:
                N_Queen(now+1,end)
            #print(queenList)

N_Queen(0,N)
print(ans)
#print(queenList)
    

# for -else 구문