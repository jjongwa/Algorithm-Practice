little = []
for i in range(9):
    little.append(int(input()))
tmp1, tmp2 = 0,0
for i in range(8):
    for j in range(i+1,9):
        if sum(little) - little[i] - little[j] == 100:
            tmp1 = little[i]
            tmp2 = little[j]

little.remove(tmp1)
little.remove(tmp2)
little.sort()

for i in little:
    print(i)