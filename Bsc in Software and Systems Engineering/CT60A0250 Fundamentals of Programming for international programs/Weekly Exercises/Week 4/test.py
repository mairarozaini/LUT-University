n = int(input("Enter a non-negative integer:\n"))

product = 1
if(n >= 0):
    for i in range(n):
        product = product * (i + 1)
    print(f"Factorial of {n} is", product)

elif(n <= 0):
    print("Error: Factorial is not defined for negative numbers")
