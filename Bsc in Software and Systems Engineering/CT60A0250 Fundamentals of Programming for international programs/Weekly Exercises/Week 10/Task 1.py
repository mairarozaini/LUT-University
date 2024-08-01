def input_integer():
    while True:
        try:
            round = input("Enter an integer:\n")
            return int(round)
        except:
            print("Invalid input. Please enter an integer.")
            return None
        
def main():
    while True:
        total = input_integer()

        if total is not None:
            print(f"Now give {total} integers!")
            sum = 0
            for i in range(total):
                n = input_integer()
                if n is not None:
                    sum += n
                else:
                    i -= 1
                
            print(f"The sum of the entered integers is: {sum}")
            break

main()
