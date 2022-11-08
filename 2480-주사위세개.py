a, b, c = map(int, input().split())
equal = 0
eNum = 0
if a == b:
    equal += 1
    eNum = a
if b == c:
    equal += 1
    eNum = b
if a == c:
    equal += 1
    eNum = a

if equal == 0:
    print(max(a, b, c) * 100)
elif equal == 1:
    print(1000 + eNum * 100)
elif equal == 3:
    print(10000 + a * 1000)
