integer = int(input("Enter a positive integer:\n"))

if integer > 0:
    numlist = list(range(2, integer, 2))
    print(*numlist, sep = "...", end = "...")
else:
    print(f"{integer} is not positive")
    
