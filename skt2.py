periods = [20, 23, 24]
payments = [[100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]]
estimates = [100000, 100000, 100000]
answer = [0,0]

for i in range(len(periods)):
    yearPaid = sum(payments[i])
    if periods[i] <24:
        nowClass = "GOLD"
    elif 23 < periods[i] < 60 and yearPaid <900000:
        nowClass = "GOLD"
    elif 59 < periods[i] and yearPaid <600000:
        nowClass = "GOLD"
    else:
        nowClass = "VIP"

    nxtPaid = yearPaid - payments[i][0] + estimates[i]

    if periods[i]+1 <24:
        nxtClass = "GOLD"
    elif 23 < periods[i]+1 < 60 and nxtPaid <900000:
        nxtClass = "GOLD"
    elif 59 < periods[i]+1 and nxtPaid <600000:
        nxtClass = "GOLD"
    else:
        nxtClass = "VIP"

    if nowClass == "GOLD" and nxtClass == "VIP":
        answer[0]+=1
    elif nowClass == "VIP" and nxtClass == "GOLD":
        answer[1]+=1