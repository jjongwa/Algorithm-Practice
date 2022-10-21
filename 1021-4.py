S = "aabcddcb"
C = [3,5,1,4,7]

def is_pellin(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return 1
    for i in range(1,len(word)-1):
        if word[i-1] == word[i+1]:
            return 1
    return 0

# S = S[:3] + '$' + S[3:]
# print(S)

for i in range(len(C)):

    new_C = C[:i+1]
    new_C.sort()
    new_S = ''
    for j in range(len(S)):
        if j in new_C:
            new_S += '$'
        new_S += S[j]
    s_list = new_S.split('$')
    ok = 0
    for s_l in s_list:
        if is_pellin(s_l):
            ok = 1

    if ok == 0:
        print(i+1)
        exit(0)