import csv


def process_grades_file(filename):
    with open(filename, 'r') as infile:
        reader = csv.reader(infile)

        #Read the header row and assign column index
        header = next(reader)
        first_name_index = header.index('First Name')
        last_name_index = header.index('Last Name')
        exam1_index = header.index('Exam 1')
        exam2_index = header.index('Exam 2')
        exam3_index = header.index('Exam 3')

        #Count the number of rows
        rows = list(reader)
        num_rows = len(rows)

        #Initialize accumulator
        total = [0, 0, 0]

        #Print header
        print('{:10s}{:10s}{:>10s}{:>10s}{:>10s}'.format(header[0], header[1], header[2], header[3], header[4]))
        print('-' * 50)

        #Process student's records
        for row in rows:
            exam1 = int(row[exam1_index])
            exam2 = int(row[exam2_index])
            exam3 = int(row[exam3_index])

            total[0] += exam1
            total[1] += exam2
            total[2] += exam3

            print('{:10s}{:10s}{:>10d}{:>10d}{:>10d}'.format(row[first_name_index], row[last_name_index], exam1,
                                                             exam2, exam3))

    return num_rows, total, header


if __name__ == "__main__":
    num_students, accumulated_scores, file_header = process_grades_file('grades.csv')

    #Calculate and display averages
    average_scores = [score / num_students for score in accumulated_scores]
    print('-' * 50)
    print('{:10s}{:10.2f}{:10.2f}{:10.2f}'.format('Average', average_scores[0], average_scores[1],
                                                  average_scores[2]))
