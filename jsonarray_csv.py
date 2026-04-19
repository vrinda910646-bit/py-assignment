import json
import csv

#data
data=[{"name":"siya","age":12},
      {"name":"riya:","age":15}]

#json file
with open("data.json","w") as f:
    json.dump(data,f)

#convert json to csv
with open("data.json","r") as json_file:
    data=json.load(json_file)

with open("output.csv","w",newline="")as csv_file:
    writer=csv.DictWriter(csv_file,filednames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("json converted to csv successfully")