import random 
import string

random.seed(8292)

LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL = string.punctuation
COMB = LETTERS + DIGITS + SPECIAL

def password_generator(password_length):
    if password_length <= 0:
        print("Password length must be a positive integer.")
    else:
        password = "".join(random.choice(COMB) for _ in range(password_length))
        return password

def main():
    while True:
        try:
            password_length = int(input("Enter the length of the password:\n"))
            password = password_generator(password_length)
            if password:
                print(f"Generated password: {password}")
            break
        except ValueError:
            print("Please enter a valid positive integer for the password length.")
main()
