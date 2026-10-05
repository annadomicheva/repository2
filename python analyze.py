count_of_students = 0
sum_math = 0
sum_python = 0
sum_english = 0
best_marks = 0

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"
with open(INPUT_FILE, "r", encoding = "utf-8") as f:
    next(f)
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        final_line = line.split(",")
        final_line[1] = int(final_line[1])
        final_line[2] = int(final_line[2])
        final_line[3] = int(final_line[3])
        sum_math += final_line[1]
        sum_python += final_line[2]
        sum_english += final_line[3]
        count_of_students += 1
        current_marks = round((final_line[1] + final_line[2] + final_line[3]) / 3)
        if current_marks > best_marks:
            best_marks = current_marks
            best_student = final_line[0]
    average_math = round(sum_math / count_of_students, 1)
    average_python = round(sum_python / count_of_students, 1)
    average_english = round(sum_english / count_of_students, 1)
with open(OUTPUT_FILE, "w", encoding = "utf-8") as f:
    f.write("Середній бал по класу:\n")
    f.write(f"math: {average_math}\n")
    f.write(f"python: {average_math}\n")
    f.write(f"english: {average_english}\n")
print("Середній бал по класу:")
print(f"math: {average_math}")
print(f"python: {average_math}")
print(f"english: {average_english}")
