import os.path
import random

def errorMsg(l_errorMsg):
    print("\n##################################################################")
    print("                           ERROR REPORT\n")
    print(l_errorMsg)
    print("\n##################################################################\n")

def testInputAsLetter(l_letter):
    if((ord(l_letter) >= 65 and ord(l_letter) <= 90) or (ord(l_letter) >= 97 and ord(l_letter) <= 122)):
        return True
    else:
        return False

def readFile(l_fileName):
    if os.path.isfile(l_fileName):
        try:
            if(l_fileName == "idioms.txt"):
                with open(l_fileName, "r", encoding="utf-16") as idiomFile:
                    #An array of strings containing the contents of 'idioms.txt'
                    return idiomFile.readlines()   
            else:
                with(open(l_fileName, "r")) as idiomFile:
                    return idiomFile.readlines()
        except FileNotFoundError:
            errorMsg("There was an error in reading the file")
    else:
        return []

if __name__ == "__main__":
    repeatGame = True
    #Introduction to the game
    print("This hangman game will increase your use of idioms.  Enjoy\n*Made by Connor Meads*\n")
    while(repeatGame):
        #Local Variables
        phrases = []
        returnToMainMenu = True

        while(returnToMainMenu):
            choiceInput = input("1 - Use my list of idioms\n2 - Type in your own custom phrase\n3 - Type in the name of the .txt file for your own custom phrases\n: ")

            if(choiceInput == '1'): #If user wants to use my file, send 'idioms.txt as the choiceInput
                phrases = readFile("idioms.txt")
            elif(choiceInput == '2'):
                while(True):
                    correctPhrase = True
                    customPhrase = input("Enter in your custom phrase or press '1' to return: ")
                    if(customPhrase == '1'):
                        break
                    for element in customPhrase: #Figure out if the custom phrase contains correct characters
                        if ((ord(element) >= 0 and ord(element) <= 31) or (ord(element) >= 33 and ord(element) <= 64) or (ord(element) >= 91 and ord(element) <= 96) or (ord(element) >= 123)):
                            correctPhrase = False
                            print("The character {0} is invalid.".format(element))
                    if(correctPhrase):
                        phrases.append(customPhrase)
                        break
                    else:
                        print("Please only enter letters and spaces.  Please try again...")

            elif(choiceInput == '3'): #If user wants to use their own file, test it for a file extension
                fileName = input("Enter in the name of the .txt file you would like to use or press 1 to return: ")
                if(fileName == '1'):
                    pass
                elif(fileName[-4:] == '.txt'): #Tests to see if the user inputted file has a '.txt. extension on it
                    phrases = readFile(fileName)
                else: #If the user inpufileNameoesn't have a '.txt' on it, smack it on
                    phrases = readFile(fileName + '.txt')

            if phrases != []: #This is correct output
                break
            else:
                print("\n...Returning to main menu...\n")
        
        #Start of the game
        showMustGoOn = True
        while(showMustGoOn):
            currentPhrase = random.choice(phrases).lower().rstrip()
            numGuesses = 0
            victoryPoints = 0
            numIncorrect = 0
            lettersInPhrase = 0
            victoryCondition = 0
            incorrectGuesses = []
            correctGuesses = []

            #Functionality to convert my chosen phrase to be hidden
            hiddenPhrase = []
            for i in currentPhrase:
                if(ord(i) != 32):
                    hiddenPhrase.append("*")
                    lettersInPhrase = lettersInPhrase + 1
                else:
                    hiddenPhrase.append(" ")

            print("\n** STARTING GAME **")
            print("-------------------\n")

            while(numIncorrect < 6):
                #Stats printed after every round
                print("Number of Guesses: ", numGuesses)
                print("Points: ", victoryPoints)
                print("Number of Incorrect Guesses: ", numIncorrect, "/6")
                print("Previous Wrong Guesses: ", incorrectGuesses)
                print("Previous Correct Guesses: ", correctGuesses, "\n")
                for items in hiddenPhrase:
                    print(items, end=" ")
                newGuess = input("\n\nPlease enter your best guess: ").lower()

                #Variables to determine if a letter is correct & win conditions
                increment = 0
                numCorrect = 0
                
                if(newGuess in correctGuesses): #Tests if the guess has already been guessed
                    print("\nYou have already guessed that!\n")
                elif(len(newGuess) > 1): #Checks if the guess is larger than 1 letter
                    if(newGuess in currentPhrase): #Checks if the guess is contained within the currentPhrase
                        i = 0
                        for letter in currentPhrase: #loops through the current phrase
                            if(letter == newGuess[0]): #checks if the first letter of the guess is equal to the letter
                                j = 0
                                tempStr = ""
                                for character in newGuess: #Loops through each letter in newGuess
                                    if((i + j) >= len(currentPhrase)): #This prevents the string from going out of scope
                                        break
                                    elif(currentPhrase[i + j] == newGuess[j]): #Checks if the guess is equal to the next few characters in currentPhrase.  Could utilize the 'find' method
                                        tempStr = tempStr + character
                                    j = j + 1
                                if(tempStr == newGuess): #Tests if the constructed string is equal to the guess
                                    correctGuesses.append(newGuess)
                                    k = 0
                                    for character in newGuess:
                                        if(hiddenPhrase[i + k] == "*"):
                                            hiddenPhrase[i + k] = character
                                            numCorrect = numCorrect + 1
                                        k = k + 1
                            i = i + 1

                elif(len(newGuess) == 1):
                    for letter in currentPhrase:
                        if(newGuess == currentPhrase[increment]): #Tests if the guessed letter is contained in the phrase
                            hiddenPhrase[increment] = newGuess #Changed the hidden phrase element to be equal to the guess
                            alreadyExists = False
                            victoryCondition = victoryCondition + 1
                            for i in correctGuesses:
                                if(i == newGuess):
                                    alreadyExists = True
                            if(alreadyExists == False): #It will only add the letter once
                                correctGuesses.append(currentPhrase[increment])
                                numCorrect = numCorrect + 1
                                victoryPoints = victoryPoints + 1
                                
                        increment = increment + 1
                if(numCorrect == 0):
                    incorrectGuesses.append(newGuess)
                    numIncorrect = numIncorrect + 1
                else:
                    victoryPoints = victoryPoints + numCorrect
                numGuesses = numGuesses + 1
                if("*" not in hiddenPhrase):
                    print("\n", currentPhrase.upper())
                    print("You Win!\n")
                    break

            if(numIncorrect == 6):
                print("\nThe phrase: ", currentPhrase.upper())
                print("Number of Incorrect Guesses: ", numIncorrect, "/6")
                print("You lose!\n")

            #Functionality to play again as well as vet responses
            improperInput = True
            while(improperInput):
                playAgain = input("Play again? (y / n): ")
                if(len(playAgain) == 1):
                    if(testInputAsLetter(playAgain)):
                        if(playAgain.lower() == 'n'):
                            improperInput = False
                            showMustGoOn = False
                            repeatGame = False
                            break
                        elif(playAgain.lower() == 'y'):
                            improperInput = False
                            showMustGoOn = False
                        elif(playAgain.lower() != 'n' and playAgain.lower() != 'y'):
                            errorMsg("Your input was a character other than 'y' or 'n'.  Please use 'y' or 'n'...")
                    else:
                        errorMsg("Your input wasn't a letter.  Please type 'y' or 'n'...")
                else:
                    errorMsg("Your input was longer than one character.  Please type a 'y' or 'n'...")
    
