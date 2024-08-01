
import csv
file = open("titanic.csv", "r")
reader = csv.reader(file, delimiter =",")

male = 0
female = 0
average_age = 0
count = 0
oldest_age = 0

for line in reader:
    line2list = str(line).split(",")
    if line2list[5] == "male":
        male += 1
    if line2list[5] == "female":
        female += 1
    if str(line2list).isdigit():
        average_age += int(line2list[6])
        count += 1
    if int(line2list[6]) > int(oldest_age):
        oldest_age = line2list[6]
    
print(f"""The number of male passengers: {male}
The number of female passengers: {female}
The average age of passengers: {average_age/count}
The age of the oldest passenger: {oldest_age}""")

