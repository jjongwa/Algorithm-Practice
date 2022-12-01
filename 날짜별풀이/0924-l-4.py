fees = [[4, 1000], [6, 1000], [21, 3000], [16, 2000], [26, 3000]]
t = 27

fees.sort(key = lambda x: (x[1], x[0]))
print(fees)
dic = {}
for f in fees:
    if f[1] not in dic:
        dic[f[1]] = [f[0],f[0]]
    else:
        if f[0] < dic[f[1]][0]:
            dic[f[1]][0] = f[0]
        elif f[0] > dic[f[1]][1]:
            dic[f[1]][1] = f[0]

a = dic[fees[0][1]][1]
b = fees[0][0]

tri= 0
tri2= 0
ans_min, ans_max = 0, 0
while True:
    print(a, b)
    for i in dic:
        tri2= 0
        if (i//b) * a < dic[i][1]:
            a+=1
            tri2 = 1
            break
        if tri == 1 and (i//b) *a < dic[i][0]:
            ans_max = a
            tri = 2
            break    
    if tri2 == 0:
        ans_min = a
        tri = 1
    if tri == 2:
        break
    

print(ans_min, ans_max)

    

print(dic)