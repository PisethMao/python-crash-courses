raw_data = "sTUDENT | 2026 | sOk pANha | 007 | 19 | 3.75"
data = raw_data.split("|")
student_id = data[0].strip().upper() + "-" + data[1].strip()
name = data[2].strip().title()
age = int(data[4].strip())
gpa = float(data[5].strip())
contains_2026 = "2026" in student_id
next_year_age = age + 1
double_gpa = gpa * 2

print("============Student Report============")
print()
print(f"Student ID:  {student_id}")
print(f"Name:  {name}")
print(f"Age:  {age}")
print(f"GPA:  {gpa:.2f}")
print()
print(f"ID contain 2026:  {contains_2026}")
print(f"Next year age:  {next_year_age}")
print(f"Double GPA:  {double_gpa}")
