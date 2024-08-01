letter = input("Do you want to stop the execution of the program (y/Y):\n")

if (letter == "Y" or letter == "y"):
    print("Bye!")
else:
    username = input("Enter username:\n")
    password = input("Enter password:\n")
    if (username == "Mark" and password == "drowssap"):
        print("User recognized.")
    else:
            print("You entered an invalid login name or password.")
            
