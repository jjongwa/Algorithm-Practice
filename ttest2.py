M = 20
load = [16, 15, 9, 17, 1, 3]

load.sort()

if load[-1] > M:
    answer = -1
else:

    st, end = 0, len(load)-1

    chk = 0
    while end >= st:
        print("st: ", st, "end: ", end)
        now = load[end]
        end -= 1
        while True:
            if now + load[st] <= M:
                now += load[st]
                st += 1
            else:
                break
        chk += 1
        
    print(chk)