def input_integers():
    input_string = input("Give integers separated by comma:\n")
    list_of_char = input_string.split(",")

    list_of_ints = []
    for ch in list_of_char:
        list_of_ints.append(int(ch))

    return list_of_ints


# TESTING
output = input_integers()
print(output)
