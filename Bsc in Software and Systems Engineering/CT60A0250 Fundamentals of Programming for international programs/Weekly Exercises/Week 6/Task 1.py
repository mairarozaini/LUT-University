def input_integers(integer):
    integer_list = []
    for numbers in integer:
        if numbers not in integer_list:
            integer_list.append(numbers)
    return integer_list

def main():
    integer = input("Give integers separated by comma:\n")
    
    original_integers = [int(i) for i in integer.split(",")]
    print("Original List:", original_integers)
    
    result = input_integers(original_integers)
    print("List with duplicates removed:", result)
main()

