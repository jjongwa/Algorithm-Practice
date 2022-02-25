T = int(input())
for _ in range(T):
    #check = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}
    check = { }
    gen = input()
    tri = 0
    if gen[0] == 'B' or gen[0] == 'C' or gen[0] == 'D' or gen[0] == 'E' or gen[0] == 'F':
        for i in range(1, len(gen)):
            if gen[i] == 'A' and gen[i] not in check:
                now = 'A'
                check[gen[i]] = 1
            elif gen[i] == 'A' and gen[i] in check and now == 'A':
                continue
            elif gen[i] == 'F' and now == 'A':
                now = 'F'
                check[gen[i]] = 1
            elif gen[i] == 'F' and gen[i] in check and now == 'F':
                continue
            elif gen[i] == 'C' and now == 'F':
                now = 'C'
                check[gen[i]] = 1
                if i == len(gen)-1:
                    tri = 1
            elif gen[i] == 'C' and gen[i] in check and now == 'C':
                if i == len(gen)-1:
                    tri = 1
                continue
            elif i == len(gen) -1 and now == 'C' and (gen[i] == 'A' or gen[i] == 'B' or gen[i] == 'C' or gen[i] == 'D' or gen[i] == 'E' or gen[i] == 'F'):
                tri = 1
            else:
                break
            
    elif gen[0] == 'A':
        now = 'A'
        check['A'] = 1
        
        for i in range(1, len(gen)):
            if gen[i] == 'A' and gen[i] not in check:
                now = 'A'
                check[gen[i]] = 1
            elif gen[i] == 'A' and gen[i] in check and now == 'A':
                continue
            elif gen[i] == 'F' and now == 'A':
                now = 'F'
                check[gen[i]] = 1
            elif gen[i] == 'F' and gen[i] in check and now == 'F':
                continue
            elif gen[i] == 'C' and now == 'F':
                now = 'C'
                check[gen[i]] = 1
                if i == len(gen)-1:
                    tri = 1
            elif gen[i] == 'C' and gen[i] in check and now == 'C':
                if i == len(gen)-1:
                    tri = 1
                continue
            elif i == len(gen) -1 and now == 'C' and (gen[i] == 'A' or gen[i] == 'B' or gen[i] == 'C' or gen[i] == 'D' or gen[i] == 'E' or gen[i] == 'F'):
                tri = 1
            else:
                break

    if tri == 1:
        print('Infected!')
    else:
        print('Good')