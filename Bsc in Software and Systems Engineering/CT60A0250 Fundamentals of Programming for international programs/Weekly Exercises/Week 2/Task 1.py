name = input("""Enter your name:
""")

integer = int(input("""Enter an integer:
"""))

float1 = float(input("""Enter a float:
"""))

power = round(float1 ** integer, 2)

print(f"""Decimal {float1} to power {integer} is {power}
Thank you for using the program {name}!""")
