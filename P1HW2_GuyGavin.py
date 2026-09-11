# Gavin Guy
# 09/11/2026
# P1HW2
# This program calculates travel expenses and the remaining budget.

budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? "))
accommodation = float(input("How much will you spend on accommodation? "))
food = float(input("How much will you spend on food? "))

total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

print()
print("Travel Destination:", destination)
print("Initial Budget:", budget)
print("Total Expenses:", total_expenses)
print("Remaining Budget:", remaining_budget)