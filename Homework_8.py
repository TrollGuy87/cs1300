while True:
    tableSize = int(input("Enter table size (1-12): "))

    if tableSize > 12:
        print("Invalid! Please enter a number between 1 and 12.")
    else:
        break

print(f"MULTIPLICATION TABLE ({tableSize}x{tableSize})")
print("==="* 9)

print("   |", end="")
for i in range(1, tableSize + 1):
    print(f"{i:4}", end="")
print("\n---+" + "----" * tableSize)

for row_num in range(1, tableSize + 1):
        print(f"{row_num:2d} |", end="")
        for col_num in range(1, tableSize + 1):
            product = row_num * col_num
            print(f"{product:4d}", end="")
        print()


numbers = [23, 8, 45, 12, 78, 34, 67, 91, 15, 52, 41, 3]
print(numbers)

first_num = 0

evenFilter = []

count_25 = 0
count_50 = 0
count_75 = 0
count_100 = 0

div_by_3 = []
total = 0

for i in numbers:
    if i > 75:
        first_num = i
        print(f"First number greater than 75: {first_num} (at position {numbers.index(first_num)})")
        break

for i in numbers:
    if i % 2 == 0:
        evenFilter.append(i)
print(f"Even numbers: {evenFilter}")


for i in numbers:
    if 76 <= i <= 100:
        count_100 += 1
    elif 51 <= i <= 75:
        count_75 += 1
    elif 26 <= i <= 50:
        count_50 += 1
    elif 0 <= i <= 25:
        count_25 += 1

print("Range 0-25:", count_25, "numbers")
print("Range 26-50:", count_50, "numbers")
print("Range 51-75:", count_75, "numbers")
print("Range 76-100:", count_100, "numbers")

for i in numbers:
    if i % 3 == 0:
        div_by_3.append(i)
        total += i

print("Numbers divisible by 3:", div_by_3)
print("Sum of these numbers:", total)

while True:
    num = int(input("Enter number: "))
    if num == -1:
        break
    numbers.append(num)

print("Updated list:", numbers)
print("New count:", len(numbers), "numbers")


students = ["Alice", "Bob", "Carol", "David", "Emma"]
assignments = ["HW1", "HW2", "Quiz1", "Exam1", "Quiz2"]

# Grades: each row is one student's grades for all assignments
grades = [
    [92, 88, 95, 87, 90], # Alice
    [78, 82, 73, 85, 80], # Bob
    [95, 91, 98, 92, 94], # Carol
    [65, 70, 68, 72, 75], # David
    [88, 85, 82, 90, 87] # Emma
]

num_students = len(students)
num_assignments = len(assignments)

def letter_grade(avg):
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"


print("Grade Table:")
print("     HW1 HW2 Quiz1 Exam1 Quiz2 AVG  Grade")
print("-" * 56)

averages = []
letter_grades = []

for i in range(num_students):
    total = 0

    print(f"{students[i]:<6}", end="")
    for g in grades[i]:
        print(f"{g:<5}", end="")
        total += g

    avg = total / num_assignments
    averages.append(avg)
    lg = letter_grade(avg)
    letter_grades.append(lg)
    print(f"{avg:5.1f} {lg}")

print()

print("Assignment Statistics:")

for a in range(num_assignments):
    total = 0
    highest = grades[0][a]
    lowest = grades[0][a]
    high_name = students[0]
    low_name = students[0]

    for i in range(num_students):
        score = grades[i][a]
        total += score

        if score > highest:
            highest = score
            high_name = students[i]
        if score < lowest:
            lowest = score
            low_name = students[i]

    class_avg = total / num_students
    print(f"{assignments[a]}: Class Avg: {class_avg:.1f} "
          f"Highest: {highest} ({high_name}) "
          f"Lowest: {lowest} ({low_name})")

print()

honor_roll = [students[i] for i in range(num_students) if averages[i] >= 90]
warning_list = [students[i] for i in range(num_students) if averages[i] < 70]

print("Special Recognition:")
print("Honor Roll (90+ average):", ", ".join(honor_roll) if honor_roll else "None")
print("Academic Warning (<70 average):", ", ".join(warning_list) if warning_list else "None")
print()

highest_avg = max(averages)
lowest_avg = min(averages)
class_average = sum(averages) / num_students

high_student = students[averages.index(highest_avg)]
low_student = students[averages.index(lowest_avg)]

print("Class Summary:")
print(f"Highest Overall Average: {high_student} ({highest_avg:.1f}%)")
print(f"Lowest Overall Average: {low_student} ({lowest_avg:.1f}%)")
print(f"Class Average: {class_average:.1f}%")
print()

distribution = {"A":0, "B":0, "C":0, "D":0, "F":0}

for lg in letter_grades:
    distribution[lg] += 1

print("Grade Distribution:")
print(f"A (90-100): {distribution['A']} students")
print(f"B (80-89):  {distribution['B']} students")
print(f"C (70-79):  {distribution['C']} students")
print(f"D (60-69):  {distribution['D']} students")
print(f"F (0-59):   {distribution['F']} students")