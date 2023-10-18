import random

p1_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
computer_choose = random.randint(0,2)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]

print("---------- PLAYER 1 CHOOSE:\n")
if p1_choose == 0:
    print(choices[0])
    if computer_choose == 0:
        result = "---------- ITS DRAWN ----------"
    elif computer_choose == 1:
        result = "---------- COMPUTER WINS ----------"
    elif computer_choose == 2:
        result = "---------- P1 WINS ----------"
elif p1_choose == 1:
    print(choices[1])
    if computer_choose == 0:
        result = "---------- P1 WINS ----------"
    elif computer_choose == 1:
        result = "---------- DRAWN ----------"
    elif computer_choose == 2:
        result = "---------- COMPUTER WINS ----------"
elif p1_choose == 2:
    print(choices[2])
    if computer_choose == 0:
        result = "---------- COMPUTER WINS ----------"
    elif computer_choose == 1:
        result = "---------- P1 WINS ----------"
    elif computer_choose == 2:
        result = "---------- DRAWN ----------"
else:
    print("cmon crl sprr")

print("---------- COMPUTER CHOOSE:\n")
if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
elif computer_choose == 2:
    print(scissors)

print("""
THE RESULT IS:""")

print(result)