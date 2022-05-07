alp, cop = 0, 0
problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]

almax, comax = 0, 0
for pro in problems:
    almax, comax = max(pro[0],almax), max(pro[1], comax)
#print(almax, comax)
#alc, coc = almax- alp, comax- cop
cnt = 0
while alp < almax and cop < comax:
    
