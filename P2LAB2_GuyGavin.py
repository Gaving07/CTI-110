# Gavin Guy
# 9/16/2026
# P2LAB2
# Using a dictionary to store user input and displays output to the user

# create a dictionary where the keys are the car names and the values are the miles per gallon
cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

# display dictionary
print(cars.keys())
print()

# get car from user
car_name = input("Enter a car: ")

# get mpg for given car
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon")

# get how many miles the user will drive
car_miles = float(input(f"how many miles will you drive the {car_name}? "))

# calculate 
gallons_needed = car_miles/car_mpg

# display results
print(f"{gallons_needed:.1f} gallon(s) of gas are needed to drive the {car_name} {car_miles} miles")

