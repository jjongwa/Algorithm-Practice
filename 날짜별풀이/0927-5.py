import copy
n,m = map(int, input().split())
words = list(map(str, input().split()))
words.sort()
ansList =[]

def chk(curr_num, n_sum, n_list):
    global ansList
    if n_sum == m:
        tmp = ''
        for i in n_list:
            tmp += words[i]
        ansList.append(tmp)
    if curr_num == n or n_sum > m:
        return
    
    tmp_list = copy.deepcopy(n_list)
    tmp_list.append(curr_num)
    chk(curr_num+1, n_sum+len(words[curr_num]), tmp_list)
    tmp_list.pop()
    chk(curr_num+1, n_sum, tmp_list)

chk(0,0,[])

if ansList:
    ansList.sort()
    print(ansList)
else:
    print(-1)