student = {'name': 'Vivek', 'course': 'Computing', 'grades': (22, 33, 44)}


def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for std_data in student_list:
        total += sum(std_data['grades'])
        count += len(std_data['grades'])
    return total / count


