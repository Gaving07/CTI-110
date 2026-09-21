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

print("------------Results------------")
print("Lowest Grade: ", min(grades))
print("Highest Grade: ", max(grades))
print("Sum of Grades: ", sum(grades))
print("Average: ", sum(grades) / len(grades))
print("-------------------------------")