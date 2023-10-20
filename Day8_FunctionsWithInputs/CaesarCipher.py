import string
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols_numbers_space = string.printable[:10] + string.printable[62:] + " "


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"


    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    
    cipher_text = ""
    for letter in text:
        indice = alphabet.index(letter)
        indexCripted = indice+shift
        if indexCripted > 25:
            indexCripted -= 26
        letter_encripted = alphabet[indexCripted]
        cipher_text += letter_encripted
    
    print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 



# part 2

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    cipher_text = ""
    for letter in text:
        indice = alphabet.index(letter)
        indexCripted = indice-shift
        if indexCripted < 0:
            indexCripted += 26
        letter_encripted = alphabet[indexCripted]
        cipher_text += letter_encripted
    
    print(f"The decoded text is {cipher_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# part 3
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

def caesar(text, shift, direction):
    cipher_text = ""
    if shift > 26:
        shift = shift % 26
    for letter in text:
        if letter in symbols_numbers_space:
            cipher_text += letter
        else:
            indice = alphabet.index(letter)
            if direction == "encode":
                indexCripted = indice+shift
                if indexCripted > 25:
                    indexCripted -= 26
            else:
                indexCripted = indice-shift
                if indexCripted < 0:
                    indexCripted += 26
            letter_encripted = alphabet[indexCripted]
            cipher_text += letter_encripted
    print(f"The {direction}d text is {cipher_text}")

from art import logo
print(logo)

response = "yes"
while response == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    Jegson = input("Type your message:\n").lower()
    Mendez = int(input("Type the shift number:\n"))
    caesar(text=Jegson, shift=Mendez, direction=direction)
    response = input("Type 'yes' if you want to go again. Otherwise type 'no' --> ")
print("Goodbye!!!!!!!!!!!!!!!!!!!!!!!")

# Part 4

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 