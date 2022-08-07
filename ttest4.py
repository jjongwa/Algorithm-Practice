from datetime import datetime
from collections import deque
n = 6
logs = ["4,1,59583400,2021-06-24 22:37:20", "0,3,22163700,2020-12-26 12:36:35", "0,2,45285000,2020-09-12 20:31:37", "4,2,35766000,2021-03-30 21:46:35", "5,2,45285000,2020-09-12 20:31:38", "1,2,49020000,2021-01-18 14:42:40", "1,4,10425000,2021-05-15 19:13:52", "5,0,88554900,2021-01-25 05:57:04", "2,5,59180800,2020-10-03 23:47:45", "0,4,52406000,2020-12-06 13:54:19", "4,0,5114900,2021-05-01 14:59:56", "1,2,98432700,2020-07-16 16:00:24", "0,2,35766000,2021-03-30 21:39:40", "2,4,10425000,2021-05-15 19:19:34", "5,0,78367100,2020-07-25 10:09:56", "2,4,52406000,2020-12-06 13:54:44", "0,3,76278400,2021-02-21 17:15:51", "0,1,6691800,2020-08-16 13:35:47", "5,1,71333100,2021-02-16 10:51:02", "1,3,27833700,2021-05-11 15:40:03", "2,1,89970900,2021-04-15 23:27:33", "0,4,83390900,2021-06-10 16:03:30", "3,5,49685300,2020-07-14 13:15:52", "5,2,28992700,2021-04-27 21:49:06", "2,4,91613700,2020-12-27 08:26:47", "3,2,49020000,2021-01-18 14:43:49", "3,0,29237500,2021-01-31 17:22:33", "1,0,86179600,2021-06-07 02:26:17", "0,4,57823200,2020-10-28 05:19:11", "5,0,39565800,2021-02-12 17:54:13"]


#diff = a[0]- a[1] 
#print(diff.days)
#print(diff.seconds)
#print(diff.seconds/60)

flist = [[0 for _ in range(n)] for _ in range(n)]

newlogs = []
for l in logs:
    tmp = l.split(",")
    newlogs.append([int(tmp[0]), int(tmp[1]), int(tmp[2]), datetime.strptime(tmp[3], "%Y-%m-%d %H:%M:%S")])

for i in range(len(newlogs)-1):
    for j in range(i+1, len(newlogs)):
        if newlogs[i][1] == newlogs[j][1] and newlogs[i][2] == newlogs[j][2] and (newlogs[i][3]-newlogs[j][3]).seconds/60 <= 10:
            print((newlogs[i][3]-newlogs[j][3]).seconds/60)
            flist[newlogs[i][0]][newlogs[j][0]] = 1
            flist[newlogs[j][0]][newlogs[i][0]] = 1
            flist[newlogs[i][0]][newlogs[i][1]] = 1
            flist[newlogs[i][1]][newlogs[i][0]] = 1
            flist[newlogs[j][0]][newlogs[i][1]] = 1
            flist[newlogs[i][1]][newlogs[j][0]] = 1

print(flist)

dq = deque()

for i in range(n+1):
    chklist = [0 for _ in range(n)]
    dq.append(i)
    chklist[i] = 1
    while dq:
        now = dq.popleft()
        for j in range(n+1):
            if chklist[j] == 0 and flist[now][j] == 1:
                chklist[j] = 1
                dq.append(j)
    print(sum(chklist))
                





