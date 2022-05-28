import sys
sys.stdin = open('input.txt', 'r')




logs = ["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]
answer = []
li = {}
plist = []
for log in logs:
    person, problem =  log.split(" ")
    if person not in plist:
        plist.append(person)
    if problem not in li:
        li[problem] = [person]
    if problem in li and person not in li[problem]:
        li[problem].append(person)



print(li)
print(plist)
for i in li:
    if len(li[i]) >= len(plist)/2:
        print(len(li[i]), len(plist)/2)
        answer.append(i)


print(answer)





'''
N, P = map(int, input().split())
for _ in range(N):
    line, fret = map(int, input().split())
'''


