# ÆÑÅä¸®¾ó
N = int(input())

fac = [0]*13
fac[0] = 1
for i in range(1,13):
    fac[i] = i * fac[i-1]

print(fac[N])

        