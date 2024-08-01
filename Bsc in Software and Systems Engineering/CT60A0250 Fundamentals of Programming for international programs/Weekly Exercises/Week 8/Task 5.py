from datetime import datetime

def valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    date = input("Enter a date in YYYY-MM-DD format:\n") 
    
    if valid_date(date):
        print(f"{date} is a valid date.")
    else:
        print(f"{date} is not a valid date.")
main()

