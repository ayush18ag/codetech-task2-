def calculate_average(grades):
    return sum(grades) / len(grades)

def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

def main():
    print("Welcome to the Student Grade Management System!")

    grades = []
    while True:
        try:
            grade = float(input("Enter a grade (or type 'done' to finish): "))
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            if len(grades) == 0:
                print("No grades entered. Exiting program.")
                return
            else:
                break

    if len(grades) == 0:
        print("No valid grades entered. Exiting program.")
        return

    average = calculate_average(grades)
    letter_grade = determine_letter_grade(average)
    gpa = calculate_gpa(average)

    print("\nGrade Report:")
    print(f"Grades entered: {grades}")
    print(f"Average grade: {average:.2f}")
    print(f"Letter grade: {letter_grade}")
    print(f"GPA: {gpa:.1f}")

if __name__ == "__main__":
    main()
