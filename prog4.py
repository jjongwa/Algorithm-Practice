

movie = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "u", "t", "s", "r", "q", "p", "b"]
ans =[]
mov = {}
hi = 0
for i in movie:
    if i not in mov:
        mov[i] = 1
    else:
        mov[i] += 1
        hi = max(mov[i], hi)
print(mov)
for i in range(hi,0,-1):
    tmp = []
    for j in mov:
        if mov[j] == i:
            tmp.append(j)
    tmp.sort()
    ans += tmp

print(ans)

'''

birth = ["1899-13-31", "19001231", "2001-09-04", "1900-02-29", "2021-5-31", "1950-11-30", "1996-02-29", "1999-11-31", "2000-02-29"]
def checksum(d):
    return d == "0" or  d == "1" or d == "2" or d == "3" or d == "4" or d == "5" or d == "6" or d == "7" or d == "8" or d == "9"

for i in birth:
    
    if len(i) != 10:
        continue
    tri = 0
    for j in range(10):
        if j == 4 or j == 7:
            continue
        if checksum(i[j]) != True:
            tri = 1
            break
    if tri == 1:
        continue
    y = int(i[:4])
    m = int(i[5:7])
    d = int(i[8:10])
    if 1900 > y or y > 2021:
        continue
    if m < 1 or m > 12:
        continue
    i
    if m == 1 or  m == 3 or  m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d <1 or d > 31:
            continue
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d < 1 or d >30:
            continue
    elif m == 2 and (y%400 == 0 or(y%4 == 0 and y%100 != 0)):
        if d < 1 or d >29:
            continue
    elif m == 2 and not(y%400 == 0 or (y%4 == 0 and y%100 != 0)):
        if d <1 or d >28:
            continue
    print(i)

'''

    
