import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)] 
for _ in range(N-1):
    A, B = map(int,input().split())
    tree[A].append(B)
    tree[B].append(A)
order = list(map(int,input().split()))
ans = 1
start = order[0]
for i in range(1,len(order)):
    print(order[i], tree[start])
    if order[i] in tree[start]:
        start = order[i]
    else:
        ans = 0
    

print(ans)
