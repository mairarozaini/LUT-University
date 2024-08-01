##########################################################################################################
# CT60A0203 Introduction to Programming - Online teaching
# Name: Nur Afiqah Humaira binti Mohd Rozaini
# Student number: 
# Email: Humaira.Mohd.Rozaini@student.lut.fi
# Date: 11/11/2023
#######################################################################################################

def add_student():
    new_new_student_record = []

    #STUDENT ID
    import csv
    import re
    from random import randint

    existing_student_ID = []

    students_file = open('students.txt', 'r')
    reader = csv.reader(students_file)

    for lines in reader:
        for words in lines:
            student_ID = [int(numbers) for numbers in re.findall(r'\b\d+\b', words)]
            existing_student_ID.append(student_ID)

    while True:
        new_student_ID = randint(10000,100000)
        if new_student_ID not in existing_student_ID:
            break

    new_new_student_record.append(new_student_ID)
    students_file.close()
   #print(new_new_student_record)

    #STUDENT NAMES
    print("Names should contain only letters and start with capital letters.")
    while True:
        first_name_input = input("Enter the first name of the student:\n")
        last_name_input = input("Enter the last name of the student:\n")

    #NOTES: Not sure if it's required but I added "(first_name_input[:0] + first_name_input[0+1:]).islower()" in the code below so the first and last name would register only one name with the first letter as capital and the rest as lower letters.
        if all([first_name_input[0].isupper(), (first_name_input[:0] + first_name_input[0+1:]).islower(), first_name_input.isalpha(), last_name_input[0].isupper(), (last_name_input[:0] + last_name_input[0+1:]).islower(), last_name_input.isalpha()]):
            break
        else: 
            print("Names should contain only letters and start with capital letters.")

    new_new_student_record.append(first_name_input)
    new_new_student_record.append(last_name_input)
    #print(new_new_student_record)

    #STUDENT YEAR
    import datetime 
    today = datetime.date.today()
    year = today.year
    new_new_student_record.append(year)
    #print(new_new_student_record)

    #STUDENT MAJOR
    student_major_list = ['CE', 'EE', 'ET', 'ME', 'SE']

    print("""Select student's major:
        CE: Computational Engineering
        EE: Electrical Engineering
        ET: Energy Technology
        ME: Mechanical Engineering
        SE: Software Engineering""")
    while True:
        student_major_selection = input("What is your selection?\n").upper()
        if student_major_selection in student_major_list:
            new_new_student_record.append(student_major_selection)
           #print(new_new_student_record)
            break
        else:
            print("Select a student major based on the list given.")

    #STUDENT EMAIL
    new_student_email = (f"{first_name_input}.{last_name_input}@lut.fi").lower()
    new_new_student_record.append(new_student_email)
    #print(new_new_student_record)

    #TRANSFER INFO
    students_file = open('students.txt', 'a')
    students_file.write(",".join(str(i) for i in new_new_student_record))
    students_file.write("\n")
    students_file.close()
    print("Student added successfully!\n")

def search_student():
    #3 CHARACTERS VERIFICATION
    while True:
        find_student_input = input("Give at least 3 characters of the students first or last name:\n").lower()
        if len(find_student_input) >= 3 and find_student_input.isalpha():
            break
    
    #SEARCH FILE
    students_file = open('students.txt', 'r')
    import csv

    line_reader = csv.DictReader(students_file, fieldnames=['stud_ID', 'name1', 'name2', 'year', 'major', 'email'], delimiter = ",")
    
    for lines in line_reader:
        if find_student_input in lines['name1'].lower() or find_student_input in lines['name2'].lower():
            print(f"Matching students:")
            print(f"ID: {lines['stud_ID']}, First name: {lines['name1']}, Last name: {lines['name2']}\n")
    
    students_file.close()

def search_course():
    #3 CHARACTERS VERIFICATION
    while True:
        find_input = input("Give at least 3 characters of the name of the course or the teacher:\n").lower()
        if len(find_input) >= 3 and find_input.isalpha():
            break
    
    #SEARCH FILE
    courses_file = open('courses.txt', 'r')
    import csv

    line_reader = csv.DictReader(courses_file, fieldnames=['course_ID', 'course_name', 'course_points', 'teacher1', 'teacher2', 'teacher3', 'teacher4', 'teacher5', 'teacher6', 'teacher7','teacher8', 'teacher9','teacher10'], delimiter = ",")
    
    search_result = ""

    for lines in line_reader:
        if find_input in str(lines['course_name']).lower() or find_input in str(lines['teacher1']).lower():
            string1 = (str(f"ID: {lines['course_ID']}, Name: {lines['course_name']}, Teacher(s): {lines['teacher1']}, {lines['teacher2']}, {lines['teacher3']}, {lines['teacher4']}, {lines['teacher5']}, {lines['teacher6']}, {lines['teacher7']}, {lines['teacher8']}, {lines['teacher9']}, {lines['teacher10']}\n").replace(", None", ""))
            if string1 not in search_result:
                search_result += string1

        if find_input in str(lines['teacher2']).lower() or find_input in str(lines['teacher3']).lower():
            string2 = (str(f"ID: {lines['course_ID']}, Name: {lines['course_name']}, Teacher(s): {lines['teacher1']}, {lines['teacher2']}, {lines['teacher3']}, {lines['teacher4']}, {lines['teacher5']}, {lines['teacher6']}, {lines['teacher7']}, {lines['teacher8']}, {lines['teacher9']}, {lines['teacher10']}\n").replace(", None", ""))
            if string2 not in search_result:
                search_result += string2
        
        if find_input in str(lines['teacher4']).lower() or find_input in str(lines['teacher5']).lower():
            string3 = (str(f"ID: {lines['course_ID']}, Name: {lines['course_name']}, Teacher(s): {lines['teacher1']}, {lines['teacher2']}, {lines['teacher3']}, {lines['teacher4']}, {lines['teacher5']}, {lines['teacher6']}, {lines['teacher7']}, {lines['teacher8']}, {lines['teacher9']}, {lines['teacher10']}\n").replace(", None", ""))
            if string3 not in search_result:
                search_result += string3

        if find_input in str(lines['teacher6']).lower() or find_input in str(lines['teacher7']).lower():
            string4 = (str(f"ID: {lines['course_ID']}, Name: {lines['course_name']}, Teacher(s): {lines['teacher1']}, {lines['teacher2']}, {lines['teacher3']}, {lines['teacher4']}, {lines['teacher5']}, {lines['teacher6']}, {lines['teacher7']}, {lines['teacher8']}, {lines['teacher9']}, {lines['teacher10']}\n").replace(", None", ""))
            if string4 not in search_result:
                search_result += string4

        if find_input in str(lines['teacher8']).lower() or find_input in str(lines['teacher9']).lower():
            string5 = (str(f"ID: {lines['course_ID']}, Name: {lines['course_name']}, Teacher(s): {lines['teacher1']}, {lines['teacher2']}, {lines['teacher3']}, {lines['teacher4']}, {lines['teacher5']}, {lines['teacher6']}, {lines['teacher7']}, {lines['teacher8']}, {lines['teacher9']}, {lines['teacher10']}\n").replace(", None", ""))
            if string5 not in search_result:
                search_result += string5

        if find_input in str(lines['teacher10']).lower():
            string6 = (str(f"ID: {lines['course_ID']}, Name: {lines['course_name']}, Teacher(s): {lines['teacher1']}, {lines['teacher2']}, {lines['teacher3']}, {lines['teacher4']}, {lines['teacher5']}, {lines['teacher6']}, {lines['teacher7']}, {lines['teacher8']}, {lines['teacher9']}, {lines['teacher10']}\n").replace(", None", ""))
            if string6 not in search_result:
                search_result += string6

    print(search_result)

    courses_file.close()

def add_course_completion():
    passed_list = []
    import csv
    from datetime import date, datetime, timedelta
    
    #SEARCH COURSE ID
    while True:
        courses_file = open('courses.txt', 'r')
        line_reader = csv.DictReader(courses_file, fieldnames=['course_ID', 'course_name', 'course_points', 'teacher1', 'teacher2', 'teacher3', 'teacher4', 'teacher5', 'teacher6', 'teacher7','teacher8', 'teacher9','teacher10'], delimiter = ",")

        found = False
        course_ID_input = input("Give the course ID:\n")
        for lines in line_reader:
            if course_ID_input == lines['course_ID']:
                passed_list.append(course_ID_input)
                found = True
                break
        if found:
            break
    
    courses_file.close()
        
    #NUMERIC VERIFICATION - STUDENT ID
    while True:
        students_file = open('students.txt', 'r')
        line_reader = csv.DictReader(students_file, fieldnames=['stud_ID', 'name1', 'name2', 'year', 'major', 'email'], delimiter = ",")

        found = False
        student_ID_input = input(f"Give the student ID:\n")
        if student_ID_input.isnumeric() and len(student_ID_input) == 5:
            for lines in line_reader:
                if student_ID_input in lines['stud_ID']:
                    passed_list.append(student_ID_input)
                    found = True
                    break
        if found:
            break
    
    students_file.close()

    #NUMERIC VERIFICATION - GRADE
    while True:
        grade_input = input("Give the grade:\n")
        if grade_input.isnumeric():
            break
            
    #SEARCH GRADE
    passed_file = open('passed.txt', 'r')
    line_reader = csv.DictReader(passed_file, fieldnames=['course_ID', 'student_ID', 'passed_date', 'grade'], delimiter = ",")
    
    new_grade = 0
    actual_grade = 0

    for lines in line_reader:
        if str(passed_list[0]) in lines['course_ID'] and str(passed_list[1]) in lines['student_ID']:
            actual_grade += int(lines['grade'])
            new_grade += 1
            #print(actual_grade)

    passed_file.close()

    #GRADE VERIFICATION
    if int(grade_input) > 5 or int(grade_input) < 1 :
        print("Grade is not a correct grade.\n")

    elif int(grade_input) < int(actual_grade):
        print(f"Student has passed this course earlier with grade {actual_grade}\n")

    elif int(grade_input) == int(actual_grade):
        print(f"Student has passed this course earlier with the same grade\n")

    elif int(grade_input) > int(actual_grade) and int(actual_grade) > 0:
        while True:
            try:
                found = False

                date_input = input("Enter a date (DD/MM/YYYY):\n")
                dates = datetime.strptime(date_input, "%d/%m/%Y").date()

                today = date.today()
                days_limit = today - timedelta(days = 30)

                if dates > today:
                    print("Input date is later than today. Try again!\n")
                    found = True
                    break

                elif dates <= days_limit:
                    print('Input date is older than 30 days. Contact "opinto".\n')
                    found = True
                    break

                else:
                    passed_list.append(date_input)
                    passed_list.append(grade_input)
                    #print(f"passed_list: {passed_list}")
                    
                    #FIND LINE INDEX, DELETE, AND APPEND NEW LINE
                    passed_file = open('passed.txt', 'r', newline = '')
                    reader = csv.reader(passed_file)
                    data = list(reader)
                    
                    line_index = []

                    for i, line in enumerate(data):
                        if len(line) >= 2 and passed_list[0] == line[0] and passed_list[1] == line[1]:
                            line_index.append(i)
                    
                    for index in reversed(line_index):
                        del data[index]
                
                    data.append(passed_list)
                    
                    passed_file.close()

                    #REWRITE FILE
                    passed_file = open('passed.txt', 'w', newline = '')
                    line_writer = csv.writer(passed_file)
                    line_writer.writerows(data)

                    passed_file.close()
                    
                    print("Input date is valid.\nRecord added!\n")
                    found = True
                    break

            except ValueError:
                print("Invalid date format. Use DD/MM/YYYY. Try again!\n")
                break

    elif new_grade == 0:
        while True:
            try:
                found = False

                date_input = input("Enter a date (DD/MM/YYYY):\n")
                dates = datetime.strptime(date_input, "%d/%m/%Y").date()

                today = date.today()
                days_limit = today - timedelta(days = 30)

                if dates > today:
                    print("Input date is later than today. Try again!\n")
                    found = True
                    break

                elif dates <= days_limit:
                    print('Input date is older than 30 days. Contact "opinto".\n')
                    found = True
                    break

                else:
                    passed_list.append(date_input)
                    passed_list.append(grade_input)
                    #print(f"passed_list: {passed_list}")

                    #ADD NEW LINE
                    passed_file = open('passed.txt', 'a')
                    passed_file.write(",".join(str(i) for i in passed_list))
                    passed_file.write("\n")
                    passed_file.close()

                    print("Input date is valid.\nRecord added!\n")

                    found = True
                    break

            except ValueError:
                print("Invalid date format. Use DD/MM/YYYY. Try again!\n")
                break

def show_student_record():
    #STUDENT ID VERIFICATION
    import csv

    major_dictionary = {
        'CE': 'Computational Engineering',
        'EE': 'Electrical Engineering',
        'ET': 'Energy Technology',
        'ME': 'Mechanical Engineering',
        'SE': 'Software Engineering'
        }
        
    total_credits = 0
    total_grade = 0
    total_courses = 0

    while True:
        students_file = open('students.txt', 'r')
        students_reader = csv.DictReader(students_file, fieldnames=['stud_ID', 'name1', 'name2', 'year', 'major', 'email'], delimiter = ",")
        
        student_ID = input("Student ID: ")
        found = False
        
        for lines in students_reader:
            for value in major_dictionary.items():
                if all([len(student_ID) == 5, student_ID.isnumeric(), student_ID in lines['stud_ID']]):
                    file_major = (lines['major'])

                    print(f"Name: {(lines['name2'])}, {(lines['name1'])}\nStarting year: {(lines['year'])}\nMajor: {(major_dictionary[file_major])}\nEmail: {(lines['email'])}\n\nPassed courses:\n")
                    found = True
                    break

        if found:
            break

    students_file.close()

    #SEARCH FILES
    passed_file = open('passed.txt', 'r')
    passed_reader = csv.DictReader(passed_file, fieldnames=['course_ID', 'student_ID', 'passed_date', 'grade'], delimiter = ",")

    courses_file = open('courses.txt', 'r')
    courses_reader = csv.DictReader(courses_file, fieldnames=['course_ID', 'course_name', 'course_points', 'teacher1', 'teacher2', 'teacher3', 'teacher4', 'teacher5', 'teacher6', 'teacher7','teacher8', 'teacher9','teacher10'], delimiter = ",")
    
    courses_dictionary = {course_line['course_ID']: course_line for course_line in courses_reader}

    try:
        for pass_line in passed_reader:
            if all ([student_ID in pass_line['student_ID'], pass_line['course_ID'] in courses_dictionary]):
                courses = courses_dictionary[pass_line['course_ID']]
                print(str(f"""Course ID: {courses['course_ID']}, Name: {courses['course_name']}, Credits: {courses['course_points']},
Date: {pass_line['passed_date']}, Teacher(s): {courses['teacher1']}, {courses['teacher2']}, {courses['teacher3']}, {courses['teacher4']}, {courses['teacher5']}, {courses['teacher6']}, {courses['teacher7']}, {courses['teacher8']}, {courses['teacher9']}, {courses['teacher10']}, grade: {pass_line['grade']}\n""").replace(", None", ""))
                        
                total_credits += int(courses['course_points'])
                total_grade += int(pass_line['grade'])
                total_courses += 1
                
        print(f"Total credits: {int(total_credits)}, average grade: {float(round(total_grade / total_courses))}\n")
    
    except ZeroDivisionError:
        print("The student has not passed any course.\n")

    passed_file.close()
    courses_file.close()

def main():
    main_selection_dictionary = {
        '1': add_student,
        '2': search_student,
        '3': search_course,
        '4': add_course_completion,
        '5': show_student_record
        }

    while True:
        print("""You may select one of the following:
        1) Add student
        2) Search student
        3) Search course
        4) Add course completion
        5) Show students's record
        0) Exit""")
        main_selection = input("What is your selection?\n")

        if main_selection == '0':
            break
        elif main_selection in main_selection_dictionary:
            main_selection_dictionary[main_selection]()
        else:
            print("Please enter a number from the selection.\n")
main()
