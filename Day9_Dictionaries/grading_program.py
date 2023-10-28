student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades
for key in student_scores:
    if student_scores[key] <= 70:
        grade_value = "Fail"
    elif student_scores[key] <= 80:
        grade_value = "Acceptable"
    elif student_scores[key] <= 90:
        grade_value = "Exceeds Expectations"
    elif student_scores[key] <= 100:
        grade_value = "Outstanding"
    student_grades[key] = grade_value

print(student_grades)