# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
input_file_name = input()

# read in the data, and for each student calculate their average grade and classification
with open(input_file_name, "r") as input_file:
    next(input_file)

    with open(input_file_name + "_out.csv", "w") as output_file:
        for line in input_file:
            student_data = line.strip().split(",")
            student_id = student_data[0]
            grades = [int(grade) for grade in student_data[1:] if grade]
            average_grade = sum(grades) / len(grades)

            if average_grade >= 70:
                classification = "1"
            elif average_grade >= 60:
                classification = "2:1"
            elif average_grade >= 50:
                classification = "2:2"
            elif average_grade >= 40:
                classification = "3"
            else:
                classification = "F"

            # Write student_id,average_grade,classification without a header.
            output_file.write(
                f"{student_id},{average_grade:.2f},{classification}\n"
            )
