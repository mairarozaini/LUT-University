
#########################################################################
# CT60A0203 Introduction to Programming - Online teaching
# Name: Padma Shreya Harika Voleti
# Student number: 001847725
# Email: Padma.voleti@student.lut.fi
# Date: 13.11.2023
# By submitting this work, I certify that
# All the code here has been written by myself
# However I discussed parts of the task that I did not understand with my friends in which they explained what it was.
# I asked websites(e.g.Geeksforgeeks) and CHATGPT ONLY as a tool to help me understand but every line has been written
# by myself
#########################################################################

import csv

# Part 1
def add_student_number():
    import csv
    from random import randint
    while True:
        result = False
        fileX = 'students.txt'
        File = open(fileX, "r")
        Reader = csv.reader(File)
        random_nr = randint(10000, 100000)
        for row in Reader:
            if str(random_nr) not in row[0]:
                student_id = random_nr
                result = True
                break
        if result:
            break

    return student_id 

def add_first_name_last_name():
    first_name=""
    last_name=""

    print("Names should only contain letters and start with capital letters.")
    while True:
        input_of_user1 = input("Enter the first name of the student:\n")
        input_of_user2 = input("Enter the last name of the student:\n")
        if all ([input_of_user1[0].isupper(), input_of_user1.isalpha(), input_of_user2[0].isupper(), input_of_user2.isalpha()]):
            break
        else:
            print("Names should contain only letters and start with capital letters.")
    first_name = input_of_user1
    last_name = input_of_user2

    email_id = (f"{first_name}.{last_name}@lut.fi").lower()
        
    return first_name, last_name, email_id

def add_student_year():
    import datetime 
    Today = datetime.date.today()
    student_year = Today.year
    
    return student_year
    
def add_student_major():
    print("Select student's major:")
    print("\tCE: Computational Engineering")
    print("\tEE: Electrical Engineering")
    print("\tET: Energy  Technology")
    print("\tME: Mechanical Engineering")
    print("\tSE: Software Engineering")
    major_selected = ""
    majorselection = input("What is your selection?\n")

    if majorselection == "CE":
        major_selected ="CE"
    elif majorselection == "EE":
        major_selected = "EE"
    elif majorselection == "ET":
        major_selected = "ET"
    elif majorselection == "ME":
        major_selected = "ME"
    elif majorselection == "SE":
        major_selected = "SE"
    else:
        print("Invalid selection.")
    
    return major_selected

def add_student():
    student_id = add_student_number()
    first_name, last_name, email_id = add_first_name_last_name()
    student_year = add_student_year()
    student_major = add_student_major()
    
    new_student_record = []
    new_student_record.append(student_id)
    new_student_record.append(first_name)
    new_student_record.append(last_name)
    new_student_record.append(student_year)
    new_student_record.append(student_major)
    new_student_record.append(email_id)
    print (new_student_record)

    fileX = 'students.txt'
    File = open(fileX, "a")
    File.write(",".join(str(a) for a in new_student_record))
    File.write("\n")
    print("Student added successfully!")

# Part 2

def searching_student():
    file_X = 'students.txt'

    while True:
        searching_student = input("Give at least 3 characters of the students first or last name:\n").upper()
        if len(searching_student) >= 3 and searching_student.isalpha():
            break

    found = False
    with open(file_X, 'r') as file:
        for line in file:
            id, first_name, last_name, std_year, course, email_id = line.strip().split(',')
            if searching_student.lower() in first_name.lower() or searching_student.lower() in last_name.lower():
                print(f"matching Students:\n ID: {id}, First Name: {first_name}, Last name: {last_name}")
                found = True

    if not found:
        print(f"Student '{searching_student}' not found in the file.")

# Part 3

def searching_course():
    import csv
    file_X = 'courses.txt'

    while True:
        searching_course_name = input("Give at least 3 characters of the name of the course or teacher:\n")
        if len(searching_course_name) >= 3 and searching_course_name.isalpha():
            break
        else:
            print("Course name should contain at least 3 alphabetical characters.")

    course_result = ""

    with open(file_X, 'r') as course_file:
        line_reader = csv.reader(course_file, delimiter = ",")
        for line in line_reader:
            if str(searching_course_name) in str(line[1]) or str(searching_course_name) in str(line[3]):
                result = (f"ID: {line[0]}, Name: {line[1]}, Teachers(s): {', '.join(line[3:])}\n")
                if result not in course_result:
                    course_result += result
            if len(line) > 4 and str(searching_course_name) in str(line[4]):
                result1 = (f"ID: {line[0]}, Name: {line[1]}, Teachers(s): {', '.join(line[3:])}\n")
                if result1 not in course_result:
                    course_result += result1
            if len(line) > 5 and str(searching_course_name) in str(line[5]):
                result2 = (f"ID: {line[0]}, Name: {line[1]}, Teachers(s): {', '.join(line[3:])}\n")
                if result2 not in course_result:
                    course_result += result2
        print(course_result)
    return None

# Part 4
import csv
from datetime import datetime

def verify_grade():
    with open('passed.txt', 'r') as File:
        Reader = csv.reader(File, delimiter=",")
        old_grade = 0        

def format_grade():
    while True:
        input_grade = input("Give the grade:")
        grade_X = int(input_grade)

        if 1 <= grade_X <= 5:
            break
        else:
            print("Grade is not a correct grade.")
    return grade_X

def formating_date():
    while True:
        add_date = input("Enter a date (DD/MM/YYYY):")
        try:
            # get the date
            date_format = datetime.strptime(add_date, '%d/%m/%Y')

            # get today's date and compare
            current_date = datetime.now()

            # Checking if the date is not later than today
            if date_format > current_date:
                print("Input date is later than today. Try again!")
            elif (current_date - date_format).days > 30:
                print("Input date is older than 30 days. Contact opinto.")
            else:
                return date_format.strftime('%d/%m/%Y')

        except ValueError:
            print("Invalid date format. Use DD/MM/YYYY. Try again!")

def course_id_format():
    while True:
        course_id = input("Give the course ID:")
        if len(course_id) == 5 and course_id.isalnum():
            break
        else:
            print("Invalid course ID.")
    return course_id

def student_ID_format():
    while True:
        student_id = input("Give the student ID:")
        if len(student_id) == 5 and student_id.isnumeric():
            break
        else:
            print("Invalid student ID.")
    return student_id

def course_Complete():
    file_path = 'passed.txt'

    course_id = course_id_format()
    student_id = student_ID_format()
    new_grade = format_grade()

    lines = []
    completion_added = False
    course_found = False

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if course_id == data[0] and student_id == data[1]:
                course_found = True
                # Check if the student has already passed the course
                old_grade = int(data[3])
                if new_grade > old_grade:
                    print("Student has passed this course earlier with grade {}. Updating the grade to {}.".format(old_grade, new_grade))
                    completion_added = True
                    data[3] = str(new_grade)
                    print("Record added!")
                else:
                    print("Student has passed this course earlier. No completion added.")
                lines.append(data)

            else:
                lines.append(data)

    if not course_found:
        current_date_valid = formating_date()
        if current_date_valid:
            lines.append([course_id, student_id, current_date_valid, str(new_grade)])
            print("Record added!")

    with open(file_path, 'w') as file:
        for record in lines:
            file.write(','.join(record) + '\n')

# Uncomment the line below to test the function
# course_Complete()

# Part 5
def show_student_record():
    student, student_ID = None, None
    while student == None:
        student_ID = input("Enter the student ID:\n")

        with open('students.txt', 'r') as students:
            student_file = list(students)
            for line in range(0, len(student_file)):
                student_inlist = (student_file[line]).split(",")
                if student_ID == student_inlist[0].strip():
                    student = student_inlist

    print(f"Student ID: {student_ID}")
    print(f"Name: {student[2]}, {student[1]}")
    print(f"Starting year: {student[3]}")

    if student[4] == "CE":
        print("Major: Computer Engineering")
    elif student[4] == "EE":
        print("Major: Electrical Engineering")
    elif student[4] == "ET":
        print("Major: Energy Technology")
    elif student[4] == "ME":
        print("Major: Mechanical Engineering")
    elif student[4] == "SE":
        print("Major: Software Engineering")

    print(f"Email: {student[5]}\n")
    print("Passed courses:\n")

    with open('passed.txt', 'r') as completed:
        with open('courses.txt', 'r') as degree:
            course = list(degree)
            passed = list(completed)
            credits = 0
            grade = 0
            count = 0
            for i in range(0, len(passed)):
                if student_ID in passed[i]:
                    list_passed = (passed[i]).split(",")
                    for n in range(0, len(course)):
                        if list_passed[0] in course[n]:
                            list_course = (course[n]).split(",")
                            print(f"Course ID: {list_course[0]}, Name: {list_course[1]}, Credits: {list_course[2]}, Date: {list_passed[2]}, Teacher(s): ", end="")
                            for y in range(3, len(list_course)):
                                print(list_course[y].strip(), end="")
                            print(f", grade: {list_passed[3]}")

                            credits = credits + int(list_course[2])
                            grade = grade + int(list_passed[3])
                            count = count + 1

        print(f"Total credits: {credits}, Average grade: {grade / count}\n ")

# main 
def mainfunction():
    while True:
        print("You may select one of the following:\n1) Add student\n2) Search student\n3) Search course\n4) Add course completion\n5) Show student's record\n0) Exit\n")
        selection1 = input("What is your selection?\n")
        if selection1 == "1":
            add_student()
        elif selection1 == "2": 
            searching_student()
        elif selection1 == "3":
            searching_course()
        elif selection1 == "4":
            course_Complete()
        elif selection1 == "5":
            show_student_record()
        elif selection1 == "0":
            print("Exiting the program")
            break
        else:
            print("Invalid selection.")

def main():
    mainfunction()

if __name__ == "__main__":
    main()