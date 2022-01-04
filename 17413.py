S = list(input())
tag = []
string =[]
tagtri = 0

for i in range(int(len(S))):
    if S[i] == '<':
        if string:
            print(''.join(reversed(string)),end='')
            string = []
        tagtri = 1
        tag.append(S[i])
    elif tagtri == 1:
        tag.append(S[i])
        if S[i] == '>':
            tagtri =0
            print(''.join(tag),end='')
            tag = []
    elif tagtri == 0 and S[i] != '<':
        if S[i] == ' ':
            print(''.join(reversed(string)),end='')
            print(' ',end='')
            string = []
        else:
            string.append(S[i])
if string:
    print(''.join(reversed(string)),end='')