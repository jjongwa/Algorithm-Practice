while(True):
    tri = list(map(int,input().split()))
    #print(tri)
    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break;
    else: 
        tri.sort()
        if tri[2]**2 == tri[1]**2 + tri[0]**2:
            print('right')
        else:
            print('wrong')
