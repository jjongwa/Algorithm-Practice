import sys
infix = list(input())
stack = []

for x in infix:
    if x.isalpha():
        print(x,end='')
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x =='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                print(stack.pop(),end='')
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                print(stack.pop(),end='')
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                print(stack.pop(),end='')
            stack.pop()
       
while stack:
    print(stack.pop(),end='')









'''
for i in infix:
    #print('-')
    if i != '+'and i !='-'and i !='/' and i !='*' and i !='(' and i !=')':
        print(i,end='') 
    else:
        if not stack:
            stack.append(i)
            #print('append', i)
        elif i == ')':
            while stack[-1] != '(':
                print(stack.pop(),end='')
            stack.pop()
        elif (i =='+' or i == '-') and (stack[-1] == '*' or stack[-1] == '/'):
            while stack:
                print(stack.pop(),end='')
            stack.append(i)
        elif (i =='+' or i == '-') and (stack[-1] == '+' or stack[-1] == '-'):
            print(stack.pop(),end='')
            stack.append(i)
        elif (i =='*' or i == '/') and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(),end='')
            stack.append(i)
        else:
            stack.append(i)
            #print('append', i)

while stack:
    print(stack.pop(),end='')

'''