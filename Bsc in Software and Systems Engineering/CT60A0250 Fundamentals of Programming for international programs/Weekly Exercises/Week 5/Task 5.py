first_string = input("Enter the first string:\n")
sec_string = input("Enter the second string:\n")

a_bool = (first_string in sec_string)
if a_bool == True:
    print("The first string can be found in the second string.")
else:
    print("The first string cannot be found in the second string.")
