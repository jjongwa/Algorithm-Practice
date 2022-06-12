p = [2, 5, 3, 1, 4]

answer = [0 for _ in range(len(p))]

i = 0
while True:
    compare = p[i]
    j = i
    for k in range(i+1,len(p)):
        if p[k] < compare:
            compare = p[k]
            j = k
    
    if i != j:
        tmp = p[i]
        p[i] = compare
        p[j] = tmp
        answer[i] += 1
        answer[j] += 1
    i +=1
    if i == len(answer):
        break
print(answer)