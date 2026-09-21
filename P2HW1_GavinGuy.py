# Gavin Guy
# 9/21/2026
# P2HW1
# 
print(" Gavin's magical travel calculator!!")
travel = []

travel.append(float(input("Enter Budget: ")))
destination = input("Enter your travel destination: ")
travel.append(float(input("How much will you spend on gas? ")))
travel.append(float(input("Approximately, how much will you need for accommodation/hotel? ")))
travel.append(float(input("Lastly, how much will you need for food? ")))

print("------------Travel-Expenses------------")
print("Location:          ", destination)
print("Initial Budget:    $" + str(travel[0]))
print("Gas Expenses:      $" + str(travel[1]))
print("Accommodation Expenses: $" + str(travel[2]))
print("Food Expenses:     $" + str(travel[3]))
print("----------------------------------------")
print("Total Expenses:    $" + str(sum(travel[1:])))
print("Remaining Budget:  $" + str(travel[0] - sum(travel[1:])))