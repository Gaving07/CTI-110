# Gavin Guy
# 10/5/2026
# P3HW2
# Salary Calculator

# Get employee information
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee pay rate: "))

# Calculate pay
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    regular_hours = hours_worked
    overtime_hours = 0
    overtime_pay = 0

regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Display output
print("\nEmployee Name:", employee_name)
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}{'Overtime Pay':<18}{'Reg Hour Pay':<18}{'Gross Pay':<15}")
print("-" * 96)
print(f"{hours_worked:<15.2f}${pay_rate:<14.2f}{overtime_hours:<15.2f}${overtime_pay:<17.2f}${regular_pay:<17.2f}${gross_pay:<15.2f}")


