N = input()
tri = 0
for i in range(len(N)-1, -1,-1):
    if tri == 0 and N[i] == '0':
        continue
    else:
        tri = 1
        print(N[i],end='')