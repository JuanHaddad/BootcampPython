import random
from hangman_art import logo, stages
from hangman_words import word_list

random_word = random.choice(word_list)

word_blanked = []

lives = 6


for i in range (0, len(random_word)):
    word_blanked.append("_")

print(logo)
while "_" in word_blanked:
    print(f"{stages[lives]}")

    if lives == 0:
        print('GAME OVER')
        break

    letter_choice = input("Choose a letter: ")[0].lower()

    if not letter_choice in word_blanked:
        have = False
        for index, letter in enumerate(random_word): 
            if letter == letter_choice:
                word_blanked[index] = letter
                if have == False:
                    have = True
        
        if not have:
            print(f"You guessed {letter_choice}, That's not in the word. You lose a life")
            lives -= 1


        if not "_" in word_blanked:
            print("YOU WIN")
    
    else:
        print(f"You've already guessed {letter_choice}")

    for letter in word_blanked:
        print(f'{letter}', end=' ')
