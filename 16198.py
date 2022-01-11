import copy
N = int(input())
energy = list(map(int,input().split()))
ans = -1e9
def DFS(sum, e_list):
    global ans
    if len(e_list) == 2:
        ans = max(sum,ans)
        return

    for i in range(1,len(e_list)-1):
        nowList = copy.deepcopy(e_list)
        del nowList[i]
        DFS(sum + e_list[i-1]*e_list[i+1], nowList)
DFS(0,energy)
print(ans)