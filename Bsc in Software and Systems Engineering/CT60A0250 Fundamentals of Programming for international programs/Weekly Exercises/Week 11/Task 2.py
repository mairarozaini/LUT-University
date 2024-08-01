def powers(x):
    square = x ** 2
    cube = x ** 3
    quad = x ** 4
    penta = x ** 5
    return (round(square, 4), round(cube, 4), round(quad, 4), round(penta, 4))

def main():
    x = float(input("Enter a number:\n"))
    power_tuple = powers(x)
    print(f"Powers of {x}:")
    print(f"x^2: {power_tuple[0]}")
    print(f"x^3: {power_tuple[1]}")
    print(f"x^4: {power_tuple[2]}")
    print(f"x^5: {power_tuple[3]}")

main()