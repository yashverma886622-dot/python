Gradebook Management System – Python (CLI)
1. Project Overview

This project is a Gradebook Analyzer created using Python.
It allows the user to enter student names and marks, and then calculates various statistics including:

Average marks

Median marks

Highest score

Lowest score

Grades for each student

Grade distribution

Pass/Fail status

Formatted result table

The program runs in a loop and can be repeated as needed.

2. Student Details

Name: Yash Verma

Roll No: 2501730159

Course: B.Tech CSE (AI/ML)

Assignment: Lab Assignment – 2

File Name: gradebook.py

3. Features Implemented

Input validation for student count and marks

Average and median calculation

Maximum and minimum score detection

Grade assignment (A, B, C, D, F)

Grade distribution summary

Pass/Fail detection based on threshold

Formatted tabular result output

Loop-based execution with user choice

4. Technologies Used

Python 3.x

Command Line Interface (CLI)

5. How to Run the Program

Ensure Python 3.x is installed on your system.

Save the script as gradebook.py.

Open a terminal or command prompt.

Run the following command:

python gradebook.py


Follow on-screen instructions.

6. Sample Input
Enter number of students: 3
Enter name: Alice
Enter marks: 92
Enter name: Bob
Enter marks: 78
Enter name: Carl
Enter marks: 55

7. Sample Output
Average Marks: 75.00
Median Marks: 78.00
Highest Score: Alice with 92 marks
Lowest Score: Carl with 55 marks
Grade Dictionary: {'Alice': 'A', 'Bob': 'C', 'Carl': 'D'}
Grade Distribution: {'A':1, 'B':0, 'C':1, 'D':1, 'F':0}
Passed Students: ['Alice', 'Bob', 'Carl']
Failed Students: []

8. File Structure
.
├── gradebook.py
└── README.md

9. Conclusion

The Gradebook Management System demonstrates the use of:

Functions

Dictionaries

Conditional statements

Loops

Input validation

CLI formatting

This assignment provides a clear understanding of basic Python programming concepts and real-world problem solving.
