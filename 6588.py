# ∞ÒµÂπŸ»Â √ﬂ√¯
import sys
list = [1]*1000001
list[1] = 0
for i in range(2,1000001,1):
    if list[i] == 1:
        for j in range(i*2,1000001,i): 
            list[j] = 0
'''
primeNum = []

for i in range(1,len(list),1):
    if list[i] == 0:
        primeNum.append(i)
'''
'''
ans = [[0,0]]*500001

for i in range(1,500001,1):
    n = i*2
    for j in primeNum:
        if n-j  in primeNum:
            ans[i] = [j, n-j]
            break
'''
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    tri = 0
    for i in range(3,len(list)):
        if list[i] and list[n-i]:
            tri = 1
            print(n,"=", i,"+", n-i)
            break

    if tri == 0:
        print("Goldbach's conjecture is wrong.")



'''
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    if ans[n/2] != [0,0]:
        print(ans[n/2])
    else:
        print("Goldbach's conjecture is wrong.")
'''




'''
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in primeNum:
        tri = 0
        a = i
        if n-a  in primeNum:
            print(n,'=',a,'+',n-a)
            tri = 1
            break
    
    if tri == 0:
        print("Goldbach's conjecture is wrong.")
'''    



