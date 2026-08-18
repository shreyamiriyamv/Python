def calculate_result(student):
    marks = student["marks"]
    total = sum(marks)
    average = total / len(marks)
    if any(mark < 40 for mark in marks):
        status = "FAIL"
        grade = "F"
    else:
        status = "PASS"
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"
    student["total"] = total
    student["average"] = average
    student["grade"] = grade
    student["status"] = status


def read_students():
    students = []
    file = open("students.csv", "r")
    for line in file:
        line = line.strip()
        data = line.split(",")
        student = {
            "roll": data[0],
            "name": data[1],
            "marks": [
                int(data[2]),
                int(data[3]),
                int(data[4])
            ]
        }
        calculate_result(student)
        students.append(student)
    file.close()
    return students


def assign_ranks(students):
    students.sort(
        key=lambda student: student["total"],
        reverse=True
    )

    rank = 1
    for student in students:
        student["rank"] = rank
        rank += 1


def display_results(students):
    print("\nSTUDENT RESULT")
    print("-" * 75)
    print(
        f"{'Rank':<6}"
        f"{'Roll':<8}"
        f"{'Name':<15}"
        f"{'Total':<8}"
        f"{'Average':<10}"
        f"{'Grade':<8}"
        f"{'Status':<8}"
    )
    print("-" * 75)
    for student in students:
        print(
            f"{student['rank']:<6}"
            f"{student['roll']:<8}"
            f"{student['name']:<15}"
            f"{student['total']:<8}"
            f"{student['average']:<10.2f}"
            f"{student['grade']:<8}"
            f"{student['status']:<8}"
        )


def write_results(students):
    file = open("student_result.csv", "w")
    file.write("STUDENT RESULT\n")
    file.write("-" * 75 + "\n")
    file.write(
        f"{'Rank':<6}"
        f"{'Roll':<8}"
        f"{'Name':<15}"
        f"{'Total':<8}"
        f"{'Average':<10}"
        f"{'Grade':<8}"
        f"{'Status':<8}\n"
    )

    file.write("-" * 75 + "\n")
    for student in students:
        file.write(
            f"{student['rank']:<6}"
            f"{student['roll']:<8}"
            f"{student['name']:<15}"
            f"{student['total']:<8}"
            f"{student['average']:<10.2f}"
            f"{student['grade']:<8}"
            f"{student['status']:<8}\n"
        )
    file.close()


students = read_students()
assign_ranks(students)
display_results(students)
write_results(students)
print("\nResult successfully saved in student_result.csv")
