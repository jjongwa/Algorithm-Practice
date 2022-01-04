#   소인수분해
'''
primeNum = [False, False] + [True] *9999999
for i in range(2,10000001):
    if primeNum[i] == 1:
        for j in range(i*2,10000001,i): 
            primeNum[j] = 0
primenumlist= []
for i in range(len(primeNum)):
    if primeNum[i] is True:
        primenumlist.append(i)

N = int(input())

while N != 0:
    for i in primenumlist:
        if i<=N and N%i ==0:
            print(i)
            N /= i
            break
'''        
N = int(input())
i = 2
while N != 1:
    if N%i == 0:
        print(i)
        N /=i
    else:
        i += 1
        
    