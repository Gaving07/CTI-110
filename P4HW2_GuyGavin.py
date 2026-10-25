
# Gavin Guy
# 10/25/2026
# P4HW2 - Salary Calculator
# This program calculates regular pay, overtime pay, and gross pay
# for multiple employees and displays the totals.

"""
Pseudocode:
1. Set total overtime pay to 0.
2. Set total regular pay to 0.
3. Set total gross pay to 0.
4. Set employee count to 0.
5. Ask the user to enter an employee's name.
6. While the employee name is not exactly "Done":
   a. Ask for hours worked.
   b. Ask for the employee's pay rate.
   c. If hours worked are greater than 40:
      - Calculate overtime hours by subtracting 40.
      - Calculate overtime pay using the pay rate times 1.5.
      - Calculate regular pay using 40 times the pay rate.
   d. Otherwise:
      - Set overtime hours to 0.
      - Set overtime pay to 0.
      - Calculate regular pay using hours worked times pay rate.
   e. Calculate gross pay by adding regular pay and overtime pay.
   f. Display the employee's pay information.
   g. Add the employee's pay amounts to the totals.
   h. Increase the employee count by 1.
   i. Ask for the next employee's name.
7. After the user enters "Done":
   a. Display total overtime pay.
   b. Display total regular pay.
   c. Display total gross pay.
   d. Display the total number of employees.
"""

# Initialize totals
totalOverPay = 0
totalRegPay = 0
totalGrossPay = 0
employeeCount = 0

# Get the first employee's name
name = input("Enter employee's name or 'Done' to finish: ")

# Process employees until the name is exactly "Done"
while name != "Done":

    # Get employee information
    hoursWorked = float(input("Enter number of hours worked: "))
    payRate = float(input("Enter employee's pay rate: "))

    # Evaluate overtime
    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        overPay = overtimeHours * (payRate * 1.5)
        regPay = 40 * payRate
    else:
        overtimeHours = 0
        overPay = 0
        regPay = hoursWorked * payRate

    # Calculate gross pay
    grossPay = regPay + overPay

    # Display employee information
    print("-------------------------------------")
    print("Employee name:", name)
    print()
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<16}{"RegHour Pay":<16}{"Gross Pay"}')
    print("-" * 90)
    print(f'{hoursWorked:<15.2f}{payRate:<12.2f}{overtimeHours:<12.2f}${overPay:<15.2f}${regPay:<15.2f}${grossPay:.2f}')

    # Update totals
    totalOverPay = totalOverPay + overPay
    totalRegPay = totalRegPay + regPay
    totalGrossPay = totalGrossPay + grossPay
    employeeCount = employeeCount + 1

    # Ask for the next employee
    name = input("\nEnter employee's name or 'Done' to finish: ")

# Display final totals
print("\n==============================")
print("Employee Payroll Summary")
print("==============================")
print(f"Total employees entered: {employeeCount}")
print(f"Total overtime pay: ${totalOverPay:.2f}")
print(f"Total regular pay: ${totalRegPay:.2f}")
print(f"Total gross pay: ${totalGrossPay:.2f}")
