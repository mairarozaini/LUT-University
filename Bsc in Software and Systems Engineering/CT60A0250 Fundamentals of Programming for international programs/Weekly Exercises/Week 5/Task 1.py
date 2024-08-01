ch = input("Enter a character:\n")
ch = ch.lower()

ch1 = len(ch)

count = 0

if ch1 == 1:
    str = (input("Enter a string:\n"))
    str = str.lower()
    for i in range(len(str)):
        if str[i] in ch:
            count += 1
    print(f"The character '{ch}' appears {count} time(s) in the string.")
    
else:
    print("Error: Give a single character.")
        
    


