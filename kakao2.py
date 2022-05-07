from collections import deque

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

answer = -2

cnt = 0 
dq = deque()
dq += queue1 + queue2 
le, ri = sum(queue1), sum(queue2)
slash = len(queue1)

while le != ri:
    if slash == 0 or slash == len(dq):
        answer = -1
        break
    if le < ri:
        cnt += 1
        le += dq[slash]
        ri -= dq[slash]
        slash += 1
    else:
        cnt +=1
        slash -= 1
        tmp = dq.popleft() 
        le -= tmp
        ri += tmp
        
if answer == -2:
    answer = cnt

print(answer)