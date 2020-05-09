if __name__ == "__main__":
    #Introduction to the game
    print("Hello & welcome to my first real python program.\nI will be attempting to make a hangman game in the console.\nFurther reading can be found on the README.md.\nEnjoy :)")

    #Gather user settings
    while True:
        difficultySetting = input("\nSELECT A DIFFICULTY:\nEasy - 1\nMedium - 2\nHard - 3\nCustom - 4\n:")
        try:
            difficultySetting = int(difficultySetting)
            if(difficultySetting < 1 or difficultySetting > 4):
                print("**Error:  You selected a value outside of 1-4.  Please enter in a correct value")
            else:
                break
        except ValueError:
            print("**Error: You did not enter in a number between 1-4.  Please select a correct difficulty...")
    
    #Depending on the input, gather the word[s] the user will be guessing
    if(difficultySetting == 1):
        print("You selected 1")
    elif(difficultySetting == 2):
        print("you selected 2")
    elif(difficultySetting == 3):
        print("you selected 3")
    else:
        print("you selected the custom option1!")