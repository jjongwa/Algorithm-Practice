# 팩토리얼 0의 개수
facZero=[0]*501
for i in range(1,501):
    num = i
    while(num%5 == 0):
        facZero[i] +=1
        num /= 5
    facZero[i] += facZero[i-1]

N = int(input())
print(facZero[N])