import os
import csv
directory = '/Users/yuanshi/Desktop/pythonprojects'
fileList = []
for file in os.listdir(directory):
    if file.endswith(".csv"):
        fileList.append(file)

myList = []
indList = []
count = 0  #skip header in following files
for x in range(0,len(fileList)):
    with open(fileList[x],'U') as f:
        for row in f:
            if(count != 0):
                count = 0
                continue
            indList = row.split(",")
            myList.append(indList)
    count += 1

with open('result.csv','w') as f:
    a = csv.writer(f)
    a.writerows(myList)
