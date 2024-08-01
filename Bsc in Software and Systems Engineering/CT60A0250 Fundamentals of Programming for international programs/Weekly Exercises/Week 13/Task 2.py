import calendar
from datetime import date

def print_month_calendar(year, month):
    first_day = date(year, month, 1)

    first_day_weekday = first_day.weekday()
    
    _, days_in_month = calendar.monthrange(year, month)
    
    print("_____________________\n Mo Tu We Th Fr Sa Su")
    
    print(" " * 3 * first_day_weekday, end="")
    
    for day in range(1, days_in_month + 1):
        print(f"{day:3}", end="")
        
        if (first_day_weekday + day) % 7 == 0:
            print()

    if (first_day_weekday + days_in_month) % 7 != 0:
        print()

print("This program prints the calendar of a desired month.")
year = int(input("Give me the year:\n"))
month = int(input("Give the month:\n"))

print_month_calendar(year, month)