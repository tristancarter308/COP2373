import csv


def write_student_grades_to_csv(filename, num_student):
    with open(filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        #Get student's name and exam scores
        for student in range(num_student):

            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')

            exam1 = int(input('Enter score for exam 1: '))
            exam2 = int(input('Enter score for exam 2: '))
            exam3 = int(input('Enter score for exam 3: '))

            writer.writerow([first_name, last_name, exam1, exam2, exam3])

if __name__ == "__main__":
    student_amount = int(input('Enter number of students: '))
    write_student_grades_to_csv('grades.csv', student_amount)
    print("Grades have been written to grades.csv")