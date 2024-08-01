no1 = int(input("Enter the first number:\n"))
no2 = int(input("Enter the second number:\n"))
print(f"""The calculator can perform the following operations:
1) Add
2) Subtract
3) Multiply 
4) Divide
The numbers you entered are {no1} and {no2}""")
op = int(input("Select the operation (1-4):\n"))


if (op == 1):
    sum1 = no1 + no2
    print(f"Selection 1: {no1} + {no2} = {sum1}")
elif (op == 2):
    sub1 = int(no1 - no2)
    print(f"Selection 2: {no1} - {no2} = {sub1}")
elif (op == 3):
    darab = no1*no2
    print(f"Selection 3: {no1} * {no2} = {darab}")
elif (op == 4):
    if (no2 == 0):
        print("Error: Zero cannot be used as a divisor.")
    else:
        bhg = float(round(no1/no2, 2))
        print(f"Selection 4: {no1} / {no2} = {bhg}")
else:
    print("The operation was not recognized.")                             
                     
        
        
    
