def employee_dictionary(dict_list):
    name = input("Enter worker's name:\n")
    workplace = input("Enter worker's workplace:\n")
    age = input("Enter worker's age:\n")
    dictionary = {'Name': name, 'Workplace': workplace, 'Age': age}
    dict_list.append(dictionary)

def print_work_info(dict_list):
    print(f"List of Employees:")
    for x in dict_list:
        print(f"Name: {x['Name']}, Workplace: {x['Workplace']}, Age: {x['Age']}")

def main():
    employees_number = int(input("How many employees do you want to add?:\n"))
    employees = []

    for i in range(employees_number):
        employee_dictionary(employees)

    print_work_info(employees)
main()