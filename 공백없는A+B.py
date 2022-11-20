num = input()
if len(num) == 4:
    print(20)
if len(num) == 3 and num[1] == '0':
    b = int(num[2])
    print(10+b)
if len(num) == 3 and num[2] == '0':
    a = int(num[0])
    print(a+10)
if len(num) == 2:
    print(int(num[0]) + int(num[1]))
