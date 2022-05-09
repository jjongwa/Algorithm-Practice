line = "64E2"
answer = []


kb = {}
kb['Q'], kb['W'], kb['E'], kb['R'], kb['T'] = (0,0), (1,0), (2,0), (3,0), (4,0)
kb['Y'], kb['U'], kb['I'], kb['O'], kb['P'] = (5,0), (6,0), (7,0), (8,0), (9,0)
kb['1'], kb['2'], kb['3'], kb['4'], kb['5'] = (0,1), (1,1), (2,1), (3,1), (4,1)
kb['6'], kb['7'], kb['8'], kb['9'], kb['0'] = (5,1), (6,1), (7,1), (8,1), (9,1)
def mh(fing, stri):
    return abs(fing[0]- stri[0])+ abs(fing[1]- stri[1])

left, right = [0,0], [9,0]

for i in line:
    if mh(left, kb[i]) < mh(right, kb[i]):
        answer.append(0)
        left = [kb[i][0], kb[i][1]]
    elif mh(left, kb[i]) > mh(right, kb[i]):
        answer.append(1)
        right = [kb[i][0], kb[i][1]]
    else:
        if abs(kb[i][0]- left[0]) < abs(kb[i][0]-right[0]):
            answer.append(0)
            left = [kb[i][0], kb[i][1]]
        elif abs(kb[i][0]- left[0]) > abs(kb[i][0]-right[0]):
            answer.append(1)
            right = [kb[i][0], kb[i][1]]
        else:
            if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == 'Q' or i == 'W' or i == 'E' or i == 'R' or i == 'T':
                answer.append(0)
                left = [kb[i][0], kb[i][1]]
            else:
                answer.append(1)
            right = [kb[i][0], kb[i][1]]

print(answer)