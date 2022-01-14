import itertools
N = int(input())
team = []
for _ in range(N):
    team.append(list(map(int,input().split())))
people = [i for i in range(1,N+1)]
leftTeam = list(itertools.combinations(people, int(N/2)))
#print(leftTeam)
ans = 1e9
for i in range(len(leftTeam)):
    startTeam = 0
    linkTeam = 0
    rightTeam = []
    for j in range(1, N+1):
        if not j in leftTeam[i]:
            rightTeam.append(j)
    #print(rightTeam)
    s_stat = list(itertools.combinations(leftTeam[i], 2))
    l_stat = list(itertools.combinations(rightTeam, 2))
    #print(s_stat, l_stat)
    #print(team[s_stat[0][0]][s_stat[0][1]])
    for j in range(len(s_stat)):
        #print(s_stat[j], l_stat[j])
        startTeam += team[s_stat[j][0]-1][s_stat[j][1]-1]
        startTeam += team[s_stat[j][1]-1][s_stat[j][0]-1]
        linkTeam += team[l_stat[j][0]-1][l_stat[j][1]-1]
        linkTeam += team[l_stat[j][1]-1][l_stat[j][0]-1]

    ans = min(abs(startTeam - linkTeam), ans) 

print(ans)

# pypy pass