vowels = ['a', 'e', 'i', 'o', 'u']

str = input("Enter a string:\n")
str = str.lower()

count = 0
for i in range(len(str)):
        if str[i] in vowels:
            
            count += 1
print(f"Number of vowels is: {count}")
    
