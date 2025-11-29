# gradebook.py
# Name: Yash Verma
# Roll No: 2501730159
# Course: B.Tech CSE (AI/ML)
# Purpose: Gradebook Analyzer CLI - calculates stats, assigns grades, prints table
# Date: 25-Nov-2025


def calculate_average(marks_dict):
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    marks_list = sorted(marks_dict.values())
    n = len(marks_list)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (marks_list[mid - 1] + marks_list[mid]) / 2
    else:
        return marks_list[mid]

def find_max_score(marks_dict):
    if not marks_dict:
        return None, None
    student = max(marks_dict, key=marks_dict.get)
    return student, marks_dict[student]

def find_min_score(marks_dict):
    if not marks_dict:
        return None, None
    student = min(marks_dict, key=marks_dict.get)
    return student, marks_dict[student]

def print_gradebook(marks_dict):
    # Assign grades (uppercase) and return a dict of grades per student
    grade_distribution = {}
    for key, value in marks_dict.items():
        if value >= 90:
            grade = "A"
        elif value >= 80:
            grade = "B"
        elif value >= 70:
            grade = "C"
        elif value >= 60:
            grade = "D"
        else:
            grade = "F"
        grade_distribution[key] = grade
    return grade_distribution

def grade_distribution(marks_dict):
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for score in marks_dict.values():
        if score >= 90:
            distribution['A'] += 1
        elif score >= 80:
            distribution['B'] += 1
        elif score >= 70:
            distribution['C'] += 1
        elif score >= 60:
            distribution['D'] += 1
        else:
            distribution['F'] += 1
    return distribution

def pass_or_fail(marks_dict, passing_marks=40):
    results = {}
    passed = []
    failed = []
    for student, score in marks_dict.items():
        if score >= passing_marks:
            results[student] = 'Pass'
            passed.append(student)
        else:
            results[student] = 'Fail'
            failed.append(student)
    return passed, len(passed), failed, len(failed), results

def print_results_table(marks_dict, grade_dist):
    NAME_WIDTH = 20
    MARKS_WIDTH = 6
    GRADE_WIDTH = 6
    SEPARATOR = "-" * (NAME_WIDTH + MARKS_WIDTH + GRADE_WIDTH + 6)

    header = f"{'Name':<{NAME_WIDTH}} | {'Marks':>{MARKS_WIDTH}} | {'Grade':>{GRADE_WIDTH}}"
    print(header)
    print(SEPARATOR)

    for name in marks_dict:
        marks = marks_dict[name]
        grade = grade_dist.get(name, '')
        print(f"{name:<{NAME_WIDTH}} | {marks:>{MARKS_WIDTH}} | {grade:>{GRADE_WIDTH}}")

    print(SEPARATOR)
    print()  # blank line after table

# _main_
ch = input("do you want to continue? (yes/no): ").lower()  # TASK6: TO RUN THE LOOP TO ASK FOR PERMISSION

while ch == "yes":
    # TASK1: introductory prints
    print("Gradebook Management System")
    print("Presented to you by YASH VERMA from B.Tech CSE(AI/ML)-SECTION C roll no:2501730159")

    marks_dict = {}
    # get number of students with validation
    while True:
        try:
            n = int(input("Enter the number of students: ").strip())
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the number of students.")

    for i in range(n):
        student_name = input("Enter the student's name: ").strip()
        if student_name == "":
            student_name = f"Student_{i+1}"
        while True:
            try:
                student_marks = int(input("Enter the student's marks: ").strip())
                break
            except ValueError:
                print("Invalid marks. Please enter an integer value.")
        marks_dict[student_name] = student_marks

    # TASK3: calculations
    average_marks = calculate_average(marks_dict)
    print(f"Average Marks: {average_marks:.2f}")

    median_marks = calculate_median(marks_dict)
    print(f"Median Marks: {median_marks:.2f}")

    max_student, max_score = find_max_score(marks_dict)
    if max_student is not None:
        print(f"Highest Score: {max_student} with {max_score} marks")
    else:
        print("Highest Score: N/A")

    min_student, min_score = find_min_score(marks_dict)
    if min_student is not None:
        print(f"Lowest Score: {min_student} with {min_score} marks")
    else:
        print("Lowest Score: N/A")

    # TASK4: grade assignment & distribution
    grade_dist = print_gradebook(marks_dict)
    print("grade dictionary:", grade_dist)

    distribution = grade_distribution(marks_dict)
    print(f"Grade Distribution: {distribution}")

    # TASK5: pass or fail
    passed, num_passed, failed, num_failed, results = pass_or_fail(marks_dict)
    print(f"Passed Students ({num_passed}): {passed}")
    print(f"Failed Students ({num_failed}): {failed}")
    print("Results:", results)

    # print results table (TASK: table format)
    print_results_table(marks_dict, grade_dist)

    ch = input("do you want to continue? (yes/no): ").lower()  # TASK6: to ask again

print("Exiting Gradebook Management System.")
