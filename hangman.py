#an attempt at making a hangman game in my last 3 days at adtran!
#QUESTIONS
    #categories? or just words???
    #irc?
    #name the hangman?
import random


#display opening message function
def openingMessage():
    print("\n\nHello! Welcome to Hangman. Preparing man to be hung...\nDone!\n\nPreparing word...\nDone!")
    
    print("\nHope you're ready, here we go!\n\n")

#pick word function
def pickWord():
    global word
    global wordRemoving
    lines = open('words.txt').read().splitlines()
    myline =random.choice(lines)
    word = myline
    wordRemoving = word
#generate array of underscores function
def generateString():
    global wordWorking
    i = 1
    dash = "-"
    while (i < len(word)):
        wordWorking = wordWorking + dash
        i = i + 1

#play game function (wait for user input and bus it out somewhere else)
def playGame():
    pickWord()
    generateString()
    while(continuePlaying):

        showGame()
        userInput = input("Guess a letter: ")
        if (userInput in usedChars):
            continue

        inputValid = checkInput(userInput)
        usedChars = usedChars = ", " + userInput

        if(inputValid & rightGuesses < len(word)):
            correctInput(userInput)
        elif(inputValid & rightGuesses == len(word)):
            theyWin()
        elif(not inputValid & wrongGuesses <= allowedWrongGuesses):
            incorrectInput(userInput)
        elif(not inputValid & wrongGuesses > allowedWrongGuesses):
            theyLose()

    playAgain()

#check if input is in word
def checkInput(userInput):
    return (userInput in wordRemoving)

#show game board
def showGame():
    if(wrongGuesses == 0):
        print(hangmanEmpty)
    elif(wrongGuesses == 1):
        print(hangman1)
    elif(wrongGuesses == 2):
        print(hangman2)
    elif(wrongGuesses == 3):
        print (hangman3)
    elif(wrongGuesses == 4):
        print (hangman4)
    elif(wrongGuesses == 5):
        print (hangman5)
    elif(wrongGuesses == 6):
        print (hangman6)
    elif(wrongGuesses == 7):
        print (hangman7)
    elif(wrongGuesses == 8):
        print (hangman8)
    elif(wrongGuesses == 9):
        print (hangman9)
    elif(wrongGuesses == 10):
        print (hangman10)
    
    print(wordWorking)
    print("\nCharacters guessed: " + usedChars)

#user gave correct input, update string
def correctInput(userInput):
    global rightGuesses
    global wordRemoving
    global wordWorking
    rightGuesses = rightGuesses + 1
    print ("Right! :D Your guess " + userInput + " is in the word.")

    i = 0
    wordRemovingList = list(wordRemoving)
    wordWorkingList = list(wordWorking)
    while(i < len(wordRemoving)):
        if(userInput == wordRemovingList[i]):
            wordRemovingList[i] = " "
            wordWorkingList[i] = userInput
        i = i + 1
    
    wordRemoving = ""
    wordRemoving.join(wordRemovingList)

    wordWorking = ""
    wordWorking.join(wordWorkingList)

#user gave last correct input, they win
def theyWin():
    continuePlaying = False
    print("`~`~` Congrats!!!! You got the winning word: " + word + "!!!!`~`~`")

#user gave incorrect input, edit hangman and incorrect guesses
def incorrectInput(userInput):
    global wrongGuesses
    wrongGuesses = wrongGuesses + 1
    print ("Wrong >:( Your guess " + userInput + " is not in the word.\nMr. Hangman gets another body part.")
    
    remaining = allowedWrongGuesses - wrongGuesses
    if(remaining <= 4):
        print ("Warning!!! Only " + remaining + " wrong guesses remaining!")

#user maxed out guesses, they lose
def theyLose():
    global continuePlaying
    continuePlaying = False
    print("boi you dun goofed and hangman is ded. Winning word was: " + word)


#play again?
def playAgain():
    play = input("Do you want to play again? (y/n): ")
    if (play == "y" or play == "Y"):
        print ("Yay!! Here we go again!!!!!")
        playGame
    else:
        print ("Baiiiii")


#dont need a main
#GLOBAL VARIABLE string of underscores / chars
wordRemoving = ""
word = ""
wordWorking = "-"
wordLength = 0
usedChars = ""
hangmanEmpty = "   ____\n  |    |\n  |\n  |\n  |\n  |\n__|__"
hangman1 = "   ____\n  |    |\n  |   ( )\n  |\n  |\n  |\n__|__"
hangman2 = "   ____\n  |    |\n  |   ( )\n  |    |\n  |\n  |\n__|__"
hangman3 = "   ____\n  |    |\n  |   ( )\n  |   \|\n  |\n  |\n__|__"
hangman4 = "   ____\n  |    |\n  |   ( )\n  |  '\|\n  |\n  |\n__|__"
hangman5 = "   ____\n  |    |\n  |   ( )\n  |  '\|/\n  |\n  |\n__|__"
hangman6 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |\n  |\n__|__"
hangman7 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |   /\n  |\n__|__"
hangman8 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |  _/\n  |\n__|__"
hangman9 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |  _/ \\\n  |\n__|__"
hangman10 = "   ____\n  |    |\n  |   ( )\n  |  '\|/'\n  |  _/ \\_\n  |\n__|__"

#GLOBAL VARIABLE CONST max amount of guesses (how many parts does mr hangman have)
allowedWrongGuesses = 10 #head, body, arms, hands, legs, feet

#GLOBAL VARIABLE num of incorrect guesses
wrongGuesses = 0
rightGuesses = 0

#GLOBAL VARIABLE keep running game
continuePlaying = True

openingMessage()
playGame()