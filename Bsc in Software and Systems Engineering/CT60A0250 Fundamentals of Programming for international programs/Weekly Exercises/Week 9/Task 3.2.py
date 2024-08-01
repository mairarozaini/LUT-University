def main():
    import json

    students = open("students.json", "r")
    student_dict = json.load(students)

    print("Students who are 19 years old:")
    for student in student_dict:
        if student["age"] == 19:
            print(f"Student ID: {student['id']}, Age: {student['age']}")
        
        print("\nStudents whose name end with 'a':")
        for student in student_dict:
            first_name = student["name"].split()[0]
            if first_name[-1] == 'a':
                print(f"Student ID: {student['id']}, Name: {student['name']}")
        print("\nStudents who study math:")
        for student in student_dict:
            if "Math" in student["courses"]:
                print(f"Student ID: {student['id']}, Name: {student['name']}, Course: {student['courses']}")
main()