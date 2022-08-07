skills = [5, 8, 3, 1]
team = [4, 3]
k = 2
answer = 0
team.sort()

print(team[0], team[-1])




start, end = 0, k-1



start= 0
nowSum = 0 
tmpSum = 0
for x in range(k):
    nowSum += skills[x]
if start <= team[0]-1 and (start+k-1) >= team[-1]-1:
    tmpSum = nowSum*2
else:
    tmpSum = nowSum
answer = tmpSum
start += 1

print(answer, "asf")

while start+k-1 < len(skills):
    nowSum -= skills[start-1]
    nowSum += skills[start+k-1]
    if start <= team[0]-1 and (start+k-1) >= team[-1]-1:
        tmpSum = nowSum *2
    else:
        tmpSum = nowSum
    
    answer = max(tmpSum, answer)
    start +=1

    print(answer, "af")

print(answer)