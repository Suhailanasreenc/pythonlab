student = {"name": "John", "roll": 111, "register_number": 1845, "department": "MCA",
"semester": 1}

total_mark  = int(input("Enter the total Mark: "))

student["total_mark"] = total_mark


if total_mark >= 90:
    grade = "A"
elif total_mark >= 82:
    grade = "B"
elif total_mark >= 75:
    grade = "C"
elif total_mark >= 60:
    grade = "D"
elif total_mark >= 50:
    grade = "P"
else:
    grade = "F"


student["grade"] = grade

print("Grade: ",grade)


del student["roll"]

print(student)
