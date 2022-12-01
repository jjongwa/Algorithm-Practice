n_time = str(input())
x = int(input())
k = int(input())

ans = 0

def spend(h, m, xx):
    global ans
    hh, mm = int(h), int(m)
    xh, xm = xx // 60, xx % 60

    nh, nm = hh + xh, mm + xm
    if nm >= 60:
        nh += 1
        nm -= 60
    if nh >=24:
        nh -= 24
    
    nh, nm = str(nh), str(nm)
    if len(nh) == 1:
        nh = '0' + nh
    if len(nm) == 1:
        nm = '0' + nm

    if int(nh[0])+ int(nh[1]) + int(nm[0]) + int(nm[1]) == k:
        ans += 1
    return nh, nm


st_h, st_m = n_time.split(':')

chk = set()
chk.add((st_h, st_m))
while True:
    nxt_h, nxt_m = spend(st_h,st_m,x)
    if (nxt_h, nxt_m) in chk:
        break
    else:
        chk.add((nxt_h, nxt_m))
        st_h, st_m = nxt_h, nxt_m

print(ans)
print(chk)