from datetime import datetime

answer = input('Give a datetime string in format "%Y/%m/%d %H:%M:%S":\n')

try:
    dates = datetime.strptime(answer, "%Y/%m/%d %H:%M:%S")

    month = dates.strftime("%B")
    weekday = dates.strftime("%A")
    week_number = int(dates.strftime("%U")) + 1
    day_number = dates.strftime("%j")

    print(f"""Month: {month}\nWeekday: {weekday}\nWeek nr: 0{week_number}\nDay nr: {day_number}""")

except ValueError:
    print("Invalid datetime format. Please use the format \"%Y/%m/%d %H:%M:%S\".")
