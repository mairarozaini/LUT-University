import json

def access_students():
    with open('students.json', 'r') as file:
        students_data = json.load(file)
    return students_data

def filter_age(students, age):
    return [student for student in students if student['age'] == age]

def filter_ending(students, letter):
    return [student for student in students if student['name'].split()[0][-1].lower() == letter.lower()]

def filter_course(students, course):
    return [student for student in students if course in student['courses']]

def print_students(students, header):
    print(header)
    print("-" * len(header))
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}")
    print(" - - -")

def main():
    students_data = access_students('students.json')

    students_age_19 = filter_age(students_data, 19)
    print(students_age_19, "Students who are 19 years old:")
    students_name_end_a = filter_ending(students_data, 'a')
    print(students_name_end_a, "Students whose name ends with 'a':")
    students_math = filter_course(students_data, 'Math')
    print(students_math, "Students who study Math:")

main()
