print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

percentage_of_tip = (float(input("What the percentage tip would you like to give? 0, 5, 10, 12? ")) / 100) + 1

people = int(input("How many people to split the bill? "))

print(f"Each person should pay: ${round((total_bill*percentage_of_tip)/people, 2):.2f}")