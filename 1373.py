# 2진수 8진수
n = '0b' + input()
n = int(n, 2)
n = str(oct(n))
for i in range(2,len(n)):
    print(n[i],end="")


