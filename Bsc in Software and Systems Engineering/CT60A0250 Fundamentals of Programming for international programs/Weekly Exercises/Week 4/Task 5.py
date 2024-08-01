str = input("Enter a string:\n")
modify = ("")

for char in str:
    if char == "S":
        modify = modify + "Z"
    elif char == "s":
        modify = modify + "z"
    else:
        modify = modify + char
print("Modified string:", modify)
