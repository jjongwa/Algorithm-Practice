survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
answer = ''
dic = {"RT": 0, "CF":0, "JM":0, "AN":0}

for i in range(len(survey)):
    if survey[i] == "RT":
        dic["RT"] += (choices[i]- 4)
    elif survey[i] == "TR":
        dic["RT"] -= (choices[i]- 4)
    elif survey[i] == "CF":
        dic["CF"] += (choices[i]- 4)
    elif survey[i] == "FC":
        dic["CF"] -= (choices[i]- 4)
    elif survey[i] == "JM":
        dic["JM"] += (choices[i]- 4)
    elif survey[i] == "MJ":
        dic["JM"] -= (choices[i]- 4)
    elif survey[i] == "AN":
        dic["AN"] += (choices[i]- 4)
    elif survey[i] == "NA":
        dic["AN"] -= (choices[i]- 4)
print(dic)

if dic["RT"] > 0:
    answer += "T"
else:
    answer += "R"
if dic["CF"] > 0:
    answer += "F"
else:
    answer += "C"
if dic["JM"] > 0:
    answer += "M"    
else:
    answer += "J"
if dic["AN"] > 0:
    answer += "N"
else:
    answer += "A"

print(answer)