# Gavin Guy
# 9/14/2026
#P2LAB1
# calculations for a circle

# get radius from user
radius = float(input("Enter the radius: "))

print()
# Show data type of the radius
print(type(radius))

# calculate the formulas
import math
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# display diameter using f-string while showing a amount of decimal points
print(f"The diameter of the circle is: {diameter:.1f}")
print(f"The circumference of the circle is: {circumference:.2f}")
print(f"The area of the circle is: {area:.3f}")