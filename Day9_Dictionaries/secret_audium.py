from art import logo
import os
clear = lambda: os.system('cls')

print(logo)

data = {}
response = "y"
while response == "y":
    person = input("Whats your name? ")
    bid = int(input("Whats your bid? $"))
    data[person] = bid
    response = input("Are there other users? y/n --> ").lower()[0]
    clear()


maior_bid = 0
for key in data:
    if data[key] > maior_bid:
        maior_bid = data[key]
        winner = key

print(f"The winner was {winner} with the ${maior_bid} of bid!")