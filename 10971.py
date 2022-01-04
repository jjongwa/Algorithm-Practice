#   외판원 순회 2
N = int(input())


W = [list(map(int,input().split()))for _ in range(N)]
#print(arr)

V=[0]*N
M=1e10
def back_track(n,c):
    global N,W,V,M
    if c<M:
        if all(V) and n==0:
            M=min(M,c)
        for i in range(N):
            if W[n][i]>0 and not V[i]:
                V[i]+=1
                back_track(i,c+W[n][i])
                V[i]-=1
back_track(0,0)
print(M)