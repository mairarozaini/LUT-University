# This program finds out the relationship between three integers


while True:
    n1 = int(input("Enter 1st integer: "))
    n2 = int(input("Enter 2nd integer: "))
    n3 = int(input("Enter 3rd integer: "))

    if ((n1 == n2) and (n2 == n3)):
        print("n1 == n2 == n3")
    elif (n1 == n2):      # 3rd must be different
        if n1 > n3:
            print("n == n2 > n3")
        else:
            print("n1 == n2 < n3")
    elif (n1 == n3): # 2nd must be different
        if n1 > n2:
            print("n1 == n3 > n2")
        else:
            print("n1 == n3 < n2")
    elif (n2 == n3):
        print("2nd and 3nd are equal") # 2nd must be different
        if n2 > n3:
            print("2nd and 3rd are greater than 1st")
        else:
            print("1st is the greatest")

    # Now all numbers must be distinct:
    elif n1 < n2:
        if n3 < n1:
            print("n3 < n1 < n2")
        elif n3 > n2:
            print("n1 < n2 < n3")
        else:
            print("n1 < n3 < n2")

    elif n3 > n1: # here we know that n2 < n1
        print("n2 < n1 < n3")
    elif n3 < n2: # n3 < n1; n2 < n1
        print("n3 < n2 < n1")
    else:
        print("n2 < n3 < n1")

 
