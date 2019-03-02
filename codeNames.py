# File: codeNames.py
# Description:
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

    fileName = input("Please enter word list: ")
    if(fileName == ""):
        fileName = "wordlist2.txt"
    text = open(fileName, "r")
    words = []

    for line in text:
        line = line.strip()
        words.append(line)
    return words

# prints the give list
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

def getKey(wordList):
    keyList = []
    index = 0
    for i in range(NUM_CARDS):
        keyList.append(wordList[index].typeOfCard)
        index += 1
    return keyList

def turn(board, key, team):
    valid = True
    end = False
    
    wordList = []
    for i in range(len(board)):
        wordList.append(board[i].word)

    while valid == True:
        #print()
        #print("--------------------------------------------------------------------------")
        displayBoard(board)
        
        word = input("Word guess: ")
        while(word not in wordList):
            word = input("Word is not valid. Enter another guess: ")
        

        wordIndex = wordList.index(word)
        if (board[wordIndex].guessed) == False: 
            if (board[wordIndex].typeOfCard == team):
                print("Congrats that's one of your team's card")
            else:
                if (board[wordIndex].typeOfCard == "BYSTANDER"):
                    print("Sorry that's a bystander")
                elif (board[wordIndex].typeOfCard == "ASSASSIN"):
                    print("OH YIKES that's the ASSASSIN. You instantly lose")
                else:
                    print("Sorry that's the other team's card")
                valid = False
            board[wordIndex].guessed = True
        else:
            print("That card was already guessed. Please choose another card")
    return board

#checks whether red or blue team has won yet
def checkWin(team, board):
    
    count = 0
    for i in range(NUM_CARDS):
        if board[i].guessed == True and board[i].typeOfCard == team:
            count += 1

    if team == cardType.RED.name and count == cardType.RED.value:
        return True
    elif team == cardType.BLUE.name and count == cardType.BLUE.value:
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

def main():
    wordList = loadWords()
    chosenWords = selectWords(wordList)
    #displayBoard(chosenWords)
    printKey(chosenWords)

    key = getKey(chosenWords)
    lose = False
    win = False
    continuePlaying = True

    while continuePlaying == True:
        if lose!= True and win!= True:
            board = turn(chosenWords,key, 'RED')
            lose = checkLose('RED', board)
            win = checkWin('RED', board)
        else:
            continuePlaying = False

        if lose!= True and win!= True:
            board = turn(chosenWords,key, 'BLUE')
            lose = checkLose('BLUE', board)
            win = checkWin('BLUE', board)
        else:
            continuePlaying = False

    #print(CardType.RED.name)
main()
