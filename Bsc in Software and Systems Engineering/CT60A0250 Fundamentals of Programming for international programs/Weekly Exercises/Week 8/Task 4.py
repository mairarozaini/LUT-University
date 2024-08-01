from datetime import datetime

first_date = input("Enter the first date (DD.MM.YYYY):\n")
date1 = datetime.strptime(first_date, "%d.%m.%Y")

sec_date = input("Enter the second date (DD.MM.YYYY):\n")
date2 = datetime.strptime(sec_date, "%d.%m.%Y")

if date1 > date2:
    delta = date1 - date2
elif date2 > date1:
    delta = date2 - date1

print(f"The number of days between {first_date} and {sec_date} is {delta.days} days.")
