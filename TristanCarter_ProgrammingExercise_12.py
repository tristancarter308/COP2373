import numpy as np

#Tristan Carter 11/23/25
#This program will take the grades from grades.csv and analyse them using numpy.
#It will then print the statistics of the exams.


#Take grades from the CVS file and put them into a numpy array for analysis
def load_and_process_grades(filename="grades.csv"):
    try:
        #Loads data, skipping the header row and converting grades to integers
        grades_data = np.genfromtxt(filename, delimiter=',', skip_header=1, usecols=(2, 3, 4), dtype=int)
    except FileNotFoundError:
        print(f"Error: The file not found.")
        return

    #Print first 5 rows
    print("First rows of dataset:")
    print(grades_data[:5])

    #Calculate and print statistics for each exam
    print("\nStatistics for Each Exam:")
    for i in range(grades_data.shape[1]):
        exam_grades = grades_data[:, i]
        print(f"Exam {i+1}:")
        print(f"  Mean: {np.mean(exam_grades):.2f}")
        print(f"  Median: {np.median(exam_grades):.2f}")
        print(f"  Standard Deviation: {np.std(exam_grades):.2f}")
        print(f"  Minimum: {np.min(exam_grades)}")
        print(f"  Maximum: {np.max(exam_grades)}")

    #Calculate and print overall statistics
    print("\nOverall Statistics:")
    overall_grades = grades_data.flatten()
    print(f"  Mean: {np.mean(overall_grades):.2f}")
    print(f"  Median: {np.median(overall_grades):.2f}")
    print(f"  Standard Deviation: {np.std(overall_grades):.2f}")
    print(f"  Minimum: {np.min(overall_grades)}")
    print(f"  Maximum: {np.max(overall_grades)}")

    #Determine and print pass/fail for each exam
    print("\nPass/Fail:")
    total_passed = 0
    total_failed = 0
    for i in range(grades_data.shape[1]):
        exam_grades = grades_data[:, i]
        passed_students = np.sum(exam_grades >= 60)
        failed_students = len(exam_grades) - passed_students
        print(f"Exam {i+1}: Passed = {passed_students}, Failed = {failed_students}")
        total_passed += passed_students
        total_failed += failed_students

    #Calculate and print overall pass percentage
    overall_pass_percentage = (total_passed / (total_passed + total_failed)) * 100
    print(f"\nOverall Pass Percentage: {overall_pass_percentage:.2f}%")

#Execute the analysis
load_and_process_grades()