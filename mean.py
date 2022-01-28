import csv

with open("data.csv",newline="") as opend:
    readfile=csv.reader(opend)
    filedata=list(readfile)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    height=filedata[i][2]
    newdata.append(float(height))
n=len(newdata)
total=0
for x in newdata:
    total+=x
mean=total/n
print(mean)