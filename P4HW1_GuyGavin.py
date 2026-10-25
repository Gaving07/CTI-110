
# Gavin Guy
# 10/25/2026
# P4HW1 - Score Average
# This program collects scores, validates them, drops the lowest score,
# calculates the average, and displays the letter grade.

"""
Pseudocode:
1. Ask the user how many scores they want to enter.
2. Create an empty list to store valid scores.
3. Repeat for the number of scores requested:
   a. Ask the user to enter a score.
   b. While the score is outside the range of 0 to 100:
      - Display an error message.
      - Ask the user to enter a valid score.
   c. Add the valid score to the list.
4. Find and display the lowest score.
5. Remove one occurrence of the lowest score from the list.
6. Display the modified score list.
7. Calculate and display the average of the remaining scores.
8. Determine and display the letter grade.
"""

# Ask how many scores will be entered
num_scores = int(input("How many scores do you want to enter? "))

# Create a list to store scores
scores = []

# Collect scores and validate each one
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))

    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))

    scores.append(score)

# Find the lowest score
lowest_score = min(scores)
print("\n---------- Results ----------")
print(f"Lowest score  : {lowest_score}")

# Remove the lowest score
scores.remove(lowest_score)
print(f"Modified List : {scores}")

# Calculate the average of the modified list
average = sum(scores) / len(scores)
print(f"Scores Average: {average:.2f}")

# Determine the letter grade
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

print(f"Grade         : {grade}")
