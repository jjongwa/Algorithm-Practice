chk = [0 for _ in range(15000)]
chk[0] = 1
now = str(1)
while True:
    tmp = int(now)
    for i in now:
        tmp+=int(i)
    chk[tmp] = 1
    now = str(int(now)+ 1)
    if int(now) >10000:
        break

for i in range(1,10001):
    if chk[i] == 0:
        print(i)