import sys

N = int(input())
postfix = list(sys.stdin.readline())
postfix.pop()

list = []
for i in range(26):
    list.append(chr(ord('A')+i))
#print(postfix)
al = {}
for i in range(N):
  al[list[i]] = int(input())

#print(al)

stack = []
for i in postfix:
    if not(i == '+' or i == '-' or i == '*' or i == '/'):
        stack.append(al[i])
    else:
        x = stack.pop()
        y = stack.pop()
        if i == '+':
            stack.append(x+y)
        elif i == '-':
            stack.append(y-x)
        elif i == '*':
            stack.append(x*y)
        elif i == '/':
            stack.append(y/x)
    #print(stack)
print("{:.2f}".format(stack[-1]))        
         
       




