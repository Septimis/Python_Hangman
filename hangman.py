import os.path
import random

def readFile(l_fileName):
    if os.path.isfile(l_fileName):
        try:
            with open(l_fileName, "r", encoding="utf-16") as idiomFile:
                #An array of strings containing the contents of 'idioms.txt'
                return idiomFile.readlines()   
        except FileNotFoundError:
            print("There was an error in reading the file")
    else:
        return []

if __name__ == "__main__":
    #Local Variables
    phrases = []
    returnToMainMenu = True

    #Introduction to the game
    print("This hangman game will increase your use of idioms.  Enjoy\n*Made by Connor Meads*\n")
    
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
    
    #Now pick a random phrase from the choices
    currentPhrase = random.choice(phrases)
    print(currentPhrase)