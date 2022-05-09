atmos = [[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]
cnt = 0
mask = 0

for i in range(len(atmos)):
    if mask != 0:
        mask += 1
    else:
        if atmos[i][0] >=81 or atmos[i][1] >= 36:
            mask += 1
            cnt += 1
    if atmos[i][0] >=151 and atmos[i][1] >= 76:
            mask = 0
    if mask == 3:
        mask = 0

print(cnt)


