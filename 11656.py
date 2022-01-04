#접미사 배열
S = input()
list   =[]
list.append(S)
for i in range(len(S)-1):
    S = S[1:]
    list.append(S)

list.sort()
for i in list:
    print(i)