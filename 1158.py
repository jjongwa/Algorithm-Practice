N, K = input().split()

#print(N,K)

list = []
ans = []
for i in range(int(N)):
    list.append(i+1)

pointer = 0
listlen = len(list)
while  list:
    for j in range(int(K)-1):
        pointer +=1
        if pointer == listlen:
            pointer = 0
    ans.append(list[pointer])
    del list[pointer]
    if pointer == listlen-1:
        pointer = 0
    listlen -= 1

print('<',end='')
print(ans[0],end='')
for k in range(len(ans)-1):
    print(', ',end='')
    print(ans[k+1],end='')
print('>',end='')
