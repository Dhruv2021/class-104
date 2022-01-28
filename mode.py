import csv
from collections import Counter

with open("data.csv",newline="") as opend:
    readfile=csv.reader(opend)
    filedata=list(readfile)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    height=filedata[i][1]
    newdata.append(height)
data=Counter(newdata)
modedata={
    "50-60":0,
    "60-70":0,
    "70-80":0,
}
for height,occurence in data.items():
    if 50<float(height)<60:
        modedata["50-60"]+=occurence
    elif 60<float(height)<70:
        modedata["60-70"]+=occurence
    elif 70<float(height)<80:
        modedata["70-80"]+=occurence

print(modedata)

