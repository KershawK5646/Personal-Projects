# This program will generate a random insult for the user to use.

# Ask the user if they want to enter the program.
# Enter program loop
# Use RNG to determine which adjectives will be used.
# Combine insult and display it
# Ask the user if they want to get another insult


#Importing needed libraries
import random

def main():
    rollIntro()
    makeSpace()
    generateInsult = input('Would you like me to generate an insult for you? [Y]es or [N]o?') #This sets the loop status before starting

    # This is the main game loop.
    while generateInsult == 'y' or generateInsult == 'Y':

        makeSpace()

        # Create the word bank to pull from.
        # Left in a list to expand later.
        wordBank1 = ['CRUSTY', 'DANK ASS', 'SLIPPERY', 'SAD']
        wordBank2 = ['ALWAYS LOSING', 'NO MONEY HAVING', 'DAD DATING', 'POTATO SALAD EATING']
        wordBank3 = ['COUSIN FUCKER', 'WHORE', 'PARALLEL PARKER', 'MUFFIN PUNCHER']
        wordBank4 = ['SUCK MY ASS', 'EAT YOUR FAMILY', 'GENUINELY HAVE A PLEASANT DAY. I REALLY MEAN THAT', 'NUTT IN YOUR SOCK']

        # Assigns a random selection from the bank to a variable.
        word1 = random.choice(wordBank1)
        word2 = random.choice(wordBank2)
        word3 = random.choice(wordBank3)
        word4 = random.choice(wordBank4)

        # Generating and displaying the insult.
        print("LISTEN HERE YOU "+ word1+', '+  word2+ ', '+ word3+ "! YOU CAN JUST "+ word4+ '!')

        makeSpace()

        # Asking the user if they'd like to go again.
        generateInsult = input('Would you like to generate another insult? [Y]es, or [N]?')


    else:
        makeSpace()

        print('Press enter to exit the application.')
        input()

def rollIntro():
    print('This application will randomize an insult for you.')

def makeSpace():
    print('')



#Calling the program
main()
