# students score-dictionary
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Amit": 99,
    "Danny": 74,
    "Elite": 62,
}

# print student_scores dictionary
print(f'Student Scores: \n\t{student_scores}')

# generate student_grades dictionary
student_grades: dict = {}

for student_name, student_marks in student_scores.items():
    student_grade = None
    if 91 <= student_marks <= 100:
        student_grade = "Outstanding"
    elif 81 <= student_marks <= 90:
        student_grade = "Exceeds Expectation"
    elif 71 <= student_marks <= 80:
        student_grade = "Acceptable"
    elif student_marks <= 70:
        student_grade = "Fail"
    else:
        print(f"{student_marks} can't be a possible student_marks!")

    # set student_grade to corresponding student
    if student_grade is not None:
        student_grades[student_name] = student_grade
    else:
        student_grades[student_name] = None

# print student_name and corresponding grade
print('Student Grades:')
for name, grade in student_grades.items():
    print(f'\t\'{name}\': \'{grade}\'')
# print(student_grades)
