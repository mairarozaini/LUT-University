print("""This program calculates the average of the 3 numbers you enter.
The numbers can be int's or float's""")

first_number = float(input("Enter the first number:\n"))

sec_number = float(input("Enter the second number:\n"))

third_number = float(input("Enter the third number:\n"))

Sum = round(first_number + sec_number + third_number, 3)
print(f"Sum of the numbers: {Sum}")

average = Sum / 3

average1 = round(average, 3)
average2 = round(average)
average3 = int(average)

print(f"Average of the numbers (rounded to 3 decimal places): {average1}")
print(f"Average of the numbers (rounded to the closest integer): {average2}")
print(f"Average of the numbers as an integer without the decimal part: {average3}")
