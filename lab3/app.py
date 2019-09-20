import mymodules

import random


def main():
    roster = []
    for i in range(10):
        name = "name" + str(i)
        grade = random.randint(0, 100)
        stud = mymodules.Student(name, grade)
        roster.append(stud)

    for student in roster:
        student.print_student_info()

    print("Average of roster is :" + str(mymodules.average_grade(roster)))

main()


