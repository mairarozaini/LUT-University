points = float(input("Enter your number of points:\n"))

if (points >= 90 and points <= 100):
    print("Your grade is: 5")
elif (points >= 80 and points <= 89):
    print("Your grade is: 4")
elif (points >= 70 and points <= 79):
    print("Your grade is: 3")
elif (points >= 60 and points <= 69):
    print("Your grade is: 2")
elif (points >= 50 and points <= 59):
    print("Your grade is: 1")
elif (points >= 0 and points <= 49):
    print("Your grade is: 0")
