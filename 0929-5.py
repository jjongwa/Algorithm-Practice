import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
import copy
word = input()

# print(word[0:1])

cnt = 0

def spl(w, st):
    global cnt
    one = w[st:st+1]
    if one != '0':
        if len(w[st+1:]) == 0:
            cnt+= 1
        else:
            spl(w,st+1)

    if st < len(word)-2:
        two = w[st:st+2]
        if two[0] != '0' and int(two[0])*10 + int(two[1]) <= 32:
            if len(w[st+2:]) == 0:
                cnt += 1
            else:
                spl(w,st+2)

spl(word, 0)

print(cnt)