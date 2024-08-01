import math

def sine_calculation():
    angle = float(input("Enter an angle in degrees:\n"))
    sin = round(math.sin(math.radians(angle)), 3)
    print(f"The sine of {angle} degrees is {sin:.3f}")
    print("")

def cosine_calculation():
    angle = float(input("Enter an angle in degrees:\n"))
    cosine = round(math.cos(math.radians(angle)), 3)
    print(f"The cosine of {angle} degrees is {cosine:.3f}")
    print("")

def inverse_sine_calculation():
    angle = float(input("Enter the sine value:\n"))
    if -1 <= angle <= 1:
        inverse_sine = round(math.degrees(math.asin(angle)), 3)
        print(f"The inverse sine (in degrees) of {angle} is {inverse_sine:.2f}")
        print("")
    else:
        print("Invalid input. Sine value must be between -1 and 1.")
        print("")

def inverse_cosine_calculation():
    angle = float(input("Enter the cosine value:\n"))
    if -1 <= angle <= 1:
        inverse_cosine =  round(math.degrees(math.acos(angle)), 3)
        print(f"The inverse cosine (in degrees) of {angle} is {inverse_cosine:.2f}")
        print("")
    else:
        print("Invalid input. Cosine value must be between -1 and 1.")
        print("")
    
def main():

    while True:
        print("""Trigonometric Calculations:
1. Sine Calculation
2. Cosine Calculation
3. Inverse Sine Calculation
4. Inverse Cosine Calculation
5. Exit""")
        choice = input("Enter your choice (1/2/3/4/5):\n")

        if choice == '5':
            print("Bye!")
            break
        elif choice == '1':
            sine_calculation()
        elif choice == '2':
            cosine_calculation()
        elif choice == '3':
            inverse_sine_calculation()
        elif choice == '4':
            inverse_cosine_calculation()
        else:
            print("Invalid choice. Please select a valid option.\n")
    
main()