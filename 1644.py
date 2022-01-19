'''
n = int(input())
def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True
primeList = []
for i in range(n+1):
    if(isPrime(i)):
        primeList.append(i)
#print(primeList)
'''

'''
n = int(input())
prime_ox = [True for _ in range(4000001)]

#에라토스테네스의 체 알고리즘
for i in range(2, int(4000001 ** 0.5)):
    if prime_ox[i]:
        for j in range(i+i, 4000001, i):
            prime_ox[j] = False 
primeList = [i for i, j in enumerate(prime_ox) if j == True and i >=2 ]
print(primeList)


ans = 0
tmp = 0
end = 0

for start in range(len(primeList)):
    while tmp < n and end < len(primeList):
        tmp += primeList[end]
        end += 1
    if tmp == n:
        ans += 1
    tmp -= primeList[start]


print(ans)


'''
import math

n = int(input())
arr = [1 for _ in range(n+1)]
primeList = []

for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

for i in range(len(arr)):
    if arr[i] == True:
        primeList.append(i)
primeList.remove(0)
primeList.remove(1)
#print(primeList)
ans = 0
tmp = 0
end = 0

for start in range(len(primeList)):
    while tmp < n and end < len(primeList):
        tmp += primeList[end]
        end += 1
    if tmp == n:
        ans += 1
    tmp -= primeList[start]


print(ans)