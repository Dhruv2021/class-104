import csv

with open("data.csv",newline="") as opend:
    readfile=csv.reader(opend)
    filedata=list(readfile)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    height=filedata[i][1]
    newdata.append(height)
n=len(newdata)
newdata.sort()

if n%2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2+1])
    median=(median1+median2)/2

else :
    median=newdata[n//2]
print(median)
