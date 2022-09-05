n = int(input())
arr = [int(input()) for _ in range(n)]

first = list(map(int,input().split()))
second = list(map(int,input().split()))

temp = []
for i in range(n):
    if  first[0] <= i+1 <= first[1]:
        continue
    else:
        temp.append(arr[i])
arr = temp

temp = []
for i in range(len(arr)):
    if  second[0] <= i+1 <= second[1]:
        continue
    else:
        temp.append(arr[i])
arr = temp

print(len(arr))
for a in arr:
    print(a)