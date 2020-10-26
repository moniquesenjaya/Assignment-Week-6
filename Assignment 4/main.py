#Function to calculate average of numbers in a list
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total/len(numbers)

#To calculate a student's average with the weightage
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return homework*10/100 + quizzes*30/100 + tests*60/100

#Calculating the letter grade based on a number
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#calculating the weighted average of students in the list
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

eren = {
    "name": "Eren",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
}

mikasa = {
    "name": "Mikasa",
    "homework": [100, 92, 98, 100],
    "quizzes": [82, 83, 91],
    "tests": [89, 97]
}

armin = {
    "name": "Armin",
    "homework": [0, 87, 75, 22],
    "quizzes": [0, 75, 78],
    "tests": [100, 100]
}

students = [eren, mikasa, armin]

for student in students:
    print("\nHere's the student information for:")
    #Getting the key and value from the dictionary and making it a tuple to loop it.
    for key, value in student.items():
        print("{}: {}".format(key, value))

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))