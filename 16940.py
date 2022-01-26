# 16940 BFS 스페셜 저지
import sys
import queue
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)] 
tree[0].append(1)
for _ in range(N-1):
    A, B = map(int,input().split())
    tree[A].append(B)
    tree[B].append(A)
order = list(map(int,input().split()))

que = [0]
idx = 0
ans = 1
for x in order:
    while x not in tree[que[idx]]:
        idx += 1
        if idx == len(que):
            ans = 0
            break
    que.append(x)

print(ans)        




'''
N = int(input())
tree = [[] for _ in range(N+1)]
visit = [0 for _ in range(N+1)] 
for _ in range(N-1):
    A, B = map(int,input().split())
    tree[A].append(B)
    tree[B].append(A)
order = list(map(int,input().split()))
#print(tree)

def checkarr(arr):
    global visit
    c = []
    for i in arr:
        if visit[i] == 0:
            c.append(i)
    return c

visit[1] = 1
nowqueue = []
nowqueue.append(tree[1])
ans = 1
if order[0] != 1:
    print(0)
else:  
    for i in range(1, N):
        now = order[i]
        if now in nowqueue[0]:
            nowqueue[0].remove(now)
            visit[now] = 1
            #print(nowqueue[0])
            #print(checkarr(tree[now]))
            nowqueue.append(checkarr(tree[now]))
        else:
            ans = 0
            break
        if nowqueue[0] == []:
            nowqueue.remove(nowqueue[0])

        #print(nowqueue)

    print(ans)
'''