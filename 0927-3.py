n = int(input())
num = list(map(int, input().split()))

le, ri = 0, 0

dic = {}
dic[num[0]] = 1
ans = 1

while ri < len(num):
    # print(le, ri)
    if le == ri:
        ri += 1
    else:
        if num[ri] not in dic or dic[num[ri]] == 0:
            dic[num[ri]] = 1
            ri +=1
        else:
            ans = max(ans, ri-le)
            dic[num[ri]] += 1
            while dic[num[ri]] != 1:
                dic[num[le]] -= 1
                le += 1            
                # print("loop",le, ri)
            dic[num[ri]] = 1            
            ri +=1
print(ans)


    