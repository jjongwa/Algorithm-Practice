import sys

while 1: 
    string = sys.stdin.readline().rstrip('\n') 
    N, n, num, space = 0, 0, 0, 0 
    if not string: 
        break 
    for i in string: 
        if i.islower(): 
            n += 1 
        elif i.isupper(): 
            N += 1 
        elif i.isdigit(): 
            num += 1 
        elif i.isspace():
            space += 1

    sys.stdout.write('{} {} {} {}\n'.format(n,N,num,space))




''' 
small = "abcdefghijklmnopqrstuvwxyz"
big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = '1234567890'

while 1:
    string =list(sys.stdin.readline())
    if not string:
        break
    if string[-1] == '\n':
        string.pop()
    n, N, num, space = 0,0,0,0
    for i in string:
        if i == ' ':
            space += 1
        elif i in small:
            n += 1
        elif i in big:
            N += 1
        elif i in number:
            num += 1
    #print(string)
    print(n,'',N,'',num,'',space)
'''