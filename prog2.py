rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
target = 403
answer = []

from collections import deque
tmp = []
for i in range(len(rooms)):
    number = deque(rooms[i].split("]"))
    num = deque(number[0].split("["))
    num.popleft()
    tmp.append([int(num[0]), number[1]])
people = []
for i in tmp:
    people.append([abs(i[0]- target), i[1].split(",")])
#print(people)

haveroom = {}
for i in people:
    for j in i[1]:
        if j in haveroom:
            haveroom[j][0] += 1
            haveroom[j][1] = min(i[0], haveroom[j][1])
        else:
            haveroom[j] = [1, i[0]]

ans = sorted(haveroom.items(), key=lambda x: (x[1][0], x[1][1], x[0]))

#print(ans)

for i in ans:
    if i[1][1] != 0:
        answer.append(i[0])
print(answer)