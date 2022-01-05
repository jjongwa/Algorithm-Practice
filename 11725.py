import sys
sys.setrecursionlimit(10**6)

N = int(input())
ans = [0 for i in range(N+1)]
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def search(start,tree,parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            search(i,tree,parents)

search(1,tree,ans)

for i in range(2,N+1):
    print(ans[i])

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self,r):
        self.root = r
    
    def search(self, data):
        temp = self.root


root = Node(1)

N = int(input())
for case in range(N-1):
    a, b = map(int,input().split())
'''





'''
N = int(input())

ansList = [0 for i in range(N*2+2)] 
ans = [0 for i in range(N+1)]
ansList[1] = 1
for case in range(N-1):
    a, b = map(int,input().split())
    if ansList[a*2] == 0:
        ansList[a*2] = b
        ans[b] = a
    elif ansList[a*2+1] == 0:
        ansList[a*2+1] = b
        ans[b] = a
    elif ansList[b*2] == 0:
        ansList[b*2] = a
        ans[a] = b
    elif ansList[b*2+1] == 0:
        ansList[b*2+1] = a
        ans[a] = b
    print(ansList)



for i in range(2,N+1):
    print(ans[i])
print(ansList)
'''
