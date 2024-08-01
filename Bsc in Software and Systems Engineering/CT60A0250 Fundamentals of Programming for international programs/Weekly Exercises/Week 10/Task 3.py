def division():
    try:
        first_number = float(input("Enter the first number:\n"))
        second_number = float(input("Enter the second number:\n"))

        results = round(first_number / second_number, 8)
        print(f"The result of {first_number} / {second_number} is {results}")

    except ValueError:
        print("You must enter valid numbers")
    except ZeroDivisionError:
        print("You cannot divide by zero")

division()