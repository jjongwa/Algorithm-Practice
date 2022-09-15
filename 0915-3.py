n = int(input())
student = []
ans = [0 for _ in range(n+1)]

for i in range(1,n+1):
    math, english = map(int, input().split())
    student.append([math,english,i])

#student.sort(reverse=True)
student.sort(key=lambda x:(-x[0], -x[1]))
for i in range(1,n+1):
    ans[student[i-1][2]] = i

for i in range(1, n+1):
    print(ans[i])