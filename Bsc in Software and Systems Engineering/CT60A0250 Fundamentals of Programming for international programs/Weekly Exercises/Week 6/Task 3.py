def input_integers(integers):
    reversed_list = list(integers[::-1])
    return reversed_list

def main():
    integers = list(map(int, input("Give integers separated by comma:\n").split(",")))

    result = input_integers(integers)

    print(f"Reversed list: {result}")
main()
