queries = [[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]

answer = -1

def find_limit(num):
    tmp = 0
    while True:
        if 2**tmp >=num:
            return 2**tmp
        tmp +=1
cnt = 0
dic = {}
for q in queries:
    if q[0] not in dic: # 배열 번호가 처음일 때
        dic[q[0]] = [q[1], find_limit(q[1])]    # [원소 개수, 배열 크기]
    else:
        if dic[q[0]][0] + q[1] > dic[q[0]][1]:   # 배열 크기를 초과한다면
            cnt += dic[q[0]][0]
            dic[q[0]] = [dic[q[0]][0] + q[1], find_limit(dic[q[0]][0] + q[1])]
        else:
            dic[q[0]][0] += q[1]
    print(dic, cnt)
    
if cnt != 0:
    answer = cnt


print(answer)
print(2**0)