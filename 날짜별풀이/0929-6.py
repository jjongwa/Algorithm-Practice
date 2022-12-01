import copy
from itertools import permutations
from collections import deque
word = list(input())
print(word)

dic = dict()
for w in word:
    if w in dic:
        dic[w] += 1
    else:
        dic[w] = 1

ansList =[]

def bfs(n_word, w_list):
    for i in w_list:
        tmp_list = copy.deepcopy(w_list)
        if w_list[i] > 0:
            tmp_list[i] -= 1
            if len(n_word) + 1 == len(word) and n_word+i not in ansList:
                ansList.append(n_word+i)
            else:
                bfs(n_word+i, tmp_list)

bfs('', dic)
ansList.sort()

for i in range(len(ansList)):
    print(ansList[i])
    if i == 10000:
        break