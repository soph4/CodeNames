# File: codeNames.py
# Description: This program codes the game CodeNames.

import random
from enum import Enum

NUM_CARDS = 25
SIZE = 5

class CardType(Enum):
    RED = 8
    BLUE = 9
    ASSASSIN = 1
    BYSTANDER = 7

# loads the words from a given text file
def loadWords():

    #fileName = input("Please enter word list: ")
    #if(fileName == ""):
    fileName = "wordlist2.txt"
    #fileName = "cpcb_codenames_words.txt"
    text = open(fileName, "r")
    words = []

    for line in text:
        line = line.strip()
        words.append(line)
    return words

# prints the given list
def printList(wordList):

    for i in range(len(wordList)):
        wordList[i].printWord()
        print()

# randomly selects 25 words for the game
# creates a randomized list of Card objects each with an associated card type
def selectWords(wordList):
	
    chosenWords = []
    randNums = random.sample(range(len(wordList)), NUM_CARDS)
   
    index = 0
    for i in CardType:
        num = i.value
        while num > 0:
            chosenWords.append(Card(wordList[randNums[index]].lower(),i.name, False))
            num -= 1
            index += 1
    random.shuffle(chosenWords)
    return chosenWords

#displays the 25 randomly selected words
def displayBoard(chosenWords):

    print("--------------------------------------------------------------------------")
    index = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if chosenWords[index].guessed == True:
                chosenWords[index].printType()
            else:
                chosenWords[index].printWord()
            index  +=  1
        print()
    print("--------------------------------------------------------------------------")

#Card class
class Card:
    #initializes
    def __init__(self, word, typeOfCard, guessed):
        self.word = word
        self.typeOfCard = typeOfCard
        self.guessed = guessed

    #prints the card's word
    def printWord(self):
        print('{0: ^15}'.format(self.word), end="")

    def printType(self):
        print('{0: ^15}'.format(self.typeOfCard), end = "")

#prints the type for each card 
def printKey(key):
    index = 0
    for i in range(SIZE):
        for j in range(SIZE):
            #print('{0: ^15}'.format(key[index].typeOfCard), end = "")
            key[index].printType()
            index += 1
        print()

#returns a list of containing what type of card, each card is
def getKey(wordList):
    keyList = []
    index = 0
    for i in range(NUM_CARDS):
        keyList.append(wordList[index].typeOfCard)
        index += 1
    return keyList

def getBoardWords(board):
    wordList = []
    for i in range(len(board)):
        wordList.append(board[i].word)
    return wordList

def turn(board, key, team):
    valid = True

    #asks for clue from other team member
    print("The CLUE is:", getClue(board))
    wordList = getBoardWords(board)
        
    red_left = remainingCards(board, 'RED')
    blue_left = remainingCards(board, 'BLUE')

    while valid == True and (red_left > 0 and blue_left > 0):
        displayBoard(board)
        
        word = input("Word guess: ")
        while(word not in wordList):
            word = input("Word is not valid. Enter another guess: ")
        
        wordIndex = wordList.index(word)
        if (board[wordIndex].guessed) == False: 
            if (board[wordIndex].typeOfCard == team):
                print("CONGRATS", word, "is one of your team's cards")
            else:
                if (board[wordIndex].typeOfCard == "BYSTANDER"):
                    print("Sorry that's a bystander")
                elif (board[wordIndex].typeOfCard == "ASSASSIN"):
                    print("OH YIKES that's the ASSASSIN. You instantly lose")
                else:
                    print("SORRY", word, "is the other team's card. That ends your turn.")
                valid = False
            board[wordIndex].guessed = True
            printSummary(board)
        else:
            print("That card was already guessed. Please choose another card")
        red_left = remainingCards(board, 'RED')
        blue_left = remainingCards(board, 'BLUE')
    
#checks whether red or blue team has won yet
def checkWin(team, board):
    count = 0
    for i in range(NUM_CARDS):
        if board[i].guessed == True and board[i].typeOfCard == team:
            count += 1

    if team == CardType.RED.name and count == CardType.RED.value:
        return True
    elif team == CardType.BLUE.name and count == CardType.BLUE.value:
        return True
    else:
        return False

#checks if the red or blue team picked the assassin card
def checkLose(team, board):
    for i in range(NUM_CARDS):
        if board[i].guessed == True and board[i].typeOfCard == "ASSASSIN":
            return True
        else:
            return False

#team member enters clue they want to give to teammate
def getClue(board):
    clue = input("Enter clue: ")
    wordList = getBoardWords(board)
    valid = False
    while valid == False:
        # Splits the clue into individual words
        words = clue.strip().split()
        # Testing that the clue is a proper noun (First letters are capital)
        if len(words) == 2:
            if words[0][0] == words[0][0].upper() and words[1][0] == words[1][0].upper():
                valid = True
            else:
                valid = False 
                clue = input("Enter clue: ")
        # Testing that the clue is too long or too short
        elif len(words) != 1:
            print("The clue must be one word!")
            valid = False
            clue = input("Enter clue: ")
        # Testing that the clue is not already a word on the board 
        if clue in wordList:
            print("That is a word on the board. Please select another clue!")
            valid = False
            clue = input("Enter clue: ")
        else:
            valid = True
    return clue
    #does this need validation? checks for spaces? ignores if both words have capital letters?

#returns the remaining number of cards team needs to guess
def remainingCards(board, team):
    count = 0
    for i in range(NUM_CARDS):
        if board[i].guessed == True and board[i].typeOfCard == team:
            count += 1
    if CardType.RED.name == team:
        return CardType.RED.value - count
    else:
        return CardType.BLUE.value - count

# Prints how many cards each team has left to guess
def printSummary(board):
   print("The RED team has ", remainingCards(board, 'RED'), " more cards to guess")
   print("The BLUE team has ", remainingCards(board, 'BLUE'), " more cards to guess\n") 

'''def main():
    wordList = loadWords()

    #creates a list of 25 Cards
    chosenWords = selectWords(wordList)
    #printKey(chosenWords)

    key = getKey(chosenWords)
    continuePlaying = True

    while continuePlaying == True:
        displayBoard(chosenWords)
        printSummary(chosenWords)

        print("Its the RED teams turn")
        turn(chosenWords,key, 'RED')
        
        if checkLose('RED', chosenWords):
            print("The BLUE team has WON!")
            continuePlaying = False
        elif checkWin('RED', chosenWords):
            print("The RED team has WON!")
            continuePlaying = False

        if continuePlaying:
            print("\nUpdated board: ")
            displayBoard(chosenWords)
            print("\nIt's the BLUE teams turn")
            printSummary(chosenWords)
            turn(chosenWords,key, 'BLUE')

            if checkLose('BLUE', chosenWords):
                print("The RED team has won!")
                continuePlaying = False
            elif checkWin('BLUE', chosenWords):
                print("The BLUE team has WON!")
                continuePlaying = False

main()'''

# IDEAS to further improve the game
#   - add an actual timer

