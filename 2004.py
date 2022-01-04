# 조합 0의 개수
n, m = map(int,input().split())

def two(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two(n)-two(n-m)-two(m), five(n)-five(n-m)-five(m)))



'''
facZero=[0]*2000000001
for i in range(1,2000000001):
    num = i
    while(num%5 == 0):
        facZero[i] +=1
        num /= 5
    facZero[i] += facZero[i-1]

ans = facZero[n] - facZero[m] - facZero[n-m]
'''



'''
two = 0
five = 0
for i in range(n,m-1,-1):
    tmp =  i
    while tmp%5 == 0:
        five += 1
        tmp /= 5
    tmp = i
    while tmp%2 == 0:
        two += 1
        tmp /= 2

for i in range(1,m):
    tmp =  i
    while tmp%5 == 0:
        five -= 1
        tmp /= 5
    tmp = i
    while tmp%2 == 0:
        two -= 1
        tmp /= 2

if two > five:
    print(five)
else:
    print(two)
'''








'''
# ���丮�� 0�� ����
facZero=[0]*501
for i in range(1,501):
    num = i
    while(num%5 == 0):
        facZero[i] +=1
        num /= 5
    facZero[i] += facZero[i-1]

N = int(input())
print(facZero[N])
'''

        