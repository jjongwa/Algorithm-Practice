'''
line = input()
nowLen = len(line)-1
ans = 0
while nowLen > 0:
    #print('first while')
    if ans != 0:
        break
    start = 0
    while start +nowLen < len(line):
        #print('second while')
        if ans != 0:
            break
        ptr_s = start
        ptr_e = nowLen
        while ptr_s != ptr_e and ptr_s < ptr_e:
            if ans != 0:
                break
            if line[ptr_s] != line[ptr_e]:
                ans = nowLen + 1
            else:
                #print(line[ptr_s], line[ptr_e])
                ptr_s += 1
                ptr_e -= 1
            
        start += 1

    nowLen -= 1


if ans == 0:
    print(-1)
else:
    print(ans)
'''


line = input()

def isPal(arr, start, end):
    while start <end:
        if arr[start] != arr[end]:
            return 0
        start+=1
        end-=1
    return 1

if isPal(line, 0, len(line)-1) == 0:
    print(len(line))
elif isPal(line, 0, len(line)-2) == 0:
    print(len(line)-1)
else:
    print(-1)
