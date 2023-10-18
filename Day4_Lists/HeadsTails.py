#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random
tails = 0
heads = 0

for i in range(0, 5000):
    rando = random.randint(0,1)
    if rando == 0:
        heads += 1
    if rando == 1:
        tails += 1

print(f"""
Heads: {heads}
Tails: {tails}
""")
