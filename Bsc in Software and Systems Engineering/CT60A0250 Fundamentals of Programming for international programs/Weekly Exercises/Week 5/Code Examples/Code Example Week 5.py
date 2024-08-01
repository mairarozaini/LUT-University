def print_menu():
    print("\nCompute the area of:")
    print("1) a circle")  
    print("2) a rectangle")
    print("3) a triangle")
    print("4) quit")  
    return int(input("Enter your choice:\n"))

def circle_area(r):
    return 3.14159 * r**2
    
def rectangle_area(w, h):
    return w * h

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return square_root(s*(s-a)*(s-b)*(s-c)) # Heron's formula

def square_root(x):
    return x**0.5

#### MAIN PROGRAM ###

while True:
    choice = print_menu()
    
    if choice == 1: # Circle
        radius = float(input("Give the radius of a circle:\n"))

        area = circle_area(radius)
        print("The area of this circle is:", round(area,2))

    elif choice == 2: # Rectangle
        width = float(input("Give the width of a rectangle:\n"))
        height = float(input("Give the height of a rectangle:\n"))
        area = rectangle_area(width, height)
        print("The area of this rectangle is:", round(area,2))

    elif choice == 3: # triangle
        print("Give the three sides of a triangle.")
        s1 = float(input("Side 1:\n"))
        s2 = float(input("Side 2:\n"))
        s3 = float(input("Side 3:\n"))
        area = triangle_area(s1, s2, s3)
        print("The area of this triangle is:", round(area,2))

    elif choice == 4:
        print("Bye!")
        break  

    else:  
        print("Oops! No such choice.") 
