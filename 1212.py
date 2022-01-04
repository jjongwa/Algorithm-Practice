# 8진수 2진수
n = '0o' + input()
n = int(n, 8)
n = str(bin(n))
for i in range(2,len(n)):
    print(n[i],end="")
