import csv
with open("data.csv","r")as file:
    reader=csv.reader(file)
    count=sum(1 for row in reader)

print("total number of rows",count)