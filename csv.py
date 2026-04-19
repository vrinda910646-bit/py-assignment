import csv

#open csv file
file_name="data.csv"
with open(file_name, 'r') as file:
    reader=csv.reader(file)
    row_count=0

#count rows
for row in reader:
    row_count += 1
print("total number of rows in csv file:",row_count)