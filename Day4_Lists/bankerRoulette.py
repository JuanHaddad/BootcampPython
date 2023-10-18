# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
person_sorted = random.randint(0, len(names)-1)
print(f"{names[person_sorted]} is going to buy the meal today!")




# OR -----------------------------------

random_choice = random.choice(names)

print(f"{random_choice} is going to eat everything today!")