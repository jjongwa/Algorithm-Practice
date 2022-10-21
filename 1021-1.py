stack1 = [7]
stack2 = []
stack3 = [9]
stack4 = ""

while len(stack1) > 0 or len(stack2) > 0 or len(stack3) > 0:
    l1, l2, l3 = len(stack1)-1, len(stack2)-1, len(stack3)-1
    n1, n2, n3 = -1, -1, -1
    if l1 >= 0:
        n1 = stack1[l1]
    if l2 >= 0:
        n2 = stack2[l2]
    if l3 >= 0:
        n3 = stack3[l3]

    comp = [(n1, 1), (n2, 2), (n3, 3)]
    comp.sort(reverse=True)
    print(comp)
    if comp[0][1] == 1:
        stack1.pop()
    elif comp[0][1] == 2:
        stack2.pop()
    elif comp[0][1] == 3:
        stack3.pop()
    stack4 += str(comp[0][1])


print(int(stack4))
