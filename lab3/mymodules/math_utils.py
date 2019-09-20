def average_grade(roster):
    sum=0
    for student in roster:
        sum = sum + student.get_grade()

    avg = sum/len(roster)
    return avg




