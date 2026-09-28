# Gavin Guy
# 9/21/2026
# P2HW2
# Calculating and displaying grades using a dictionary 

grades = []

grades.append(float(input("Enter the test grade for Module 1: ")))
grades.append(float(input("Enter the test grade for Module 2: ")))
grades.append(float(input("Enter the test grade for Module 3: ")))
grades.append(float(input("Enter the test grade for Module 4: ")))
grades.append(float(input("Enter the test grade for Module 5: ")))
grades.append(float(input("Enter the test grade for Module 6: ")))


average = sum(grades) / len(grades)

print("------------Results------------")
print("Lowest Grade: ", min(grades))
print("Highest Grade: ", max(grades))
print("Sum of Grades: ", sum(grades))
print(f"Average: {average:.2f}")
print("-------------------------------")

# determining the letter grade average

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)