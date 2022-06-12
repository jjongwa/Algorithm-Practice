n = 5
plans = ["100 1 3", "500 4", "2000 5"]
clients = ["300 3 5", "1500 1", "100 1 3", "50 1 2"]

from collections import deque


answer = [0 for _ in range(len(clients))]

planD = []
planS = []
for i in plans:
    tmp = deque(list(i.split()))
    planD.append(int(tmp[0]))
    tmp.popleft()
    planS.append(tmp)

for i in range(1, len(planS)):
    planS[i] = planS[i] + planS[i-1]

for i in range(len(planS)):
    planS[i] = set(planS[i])
    
clientD = []
clientS = []
for i in clients:
    tmp = deque(list(i.split()))
    clientD.append(int(tmp[0]))
    tmp.popleft()
    clientS.append(set(tmp))

for i in range(len(clients)):
    for j in range(len(plans)):
        if clientD[i] <= planD[j] and clientS[i] == clientS[i].intersection(planS[j]):
            print(i, j,  clientS[i], planS[j])
            answer[i] = j+1
            break

print(answer)


