# File: codeNames.py
# Description:
import random
from enum import Enum

NUM_CARDS = 25
SIZE = 5

class CardType(Enum):
    RED = 8
    BLUE = 9
    ASSASIN = 1
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
def selectWords(wordList):
	
    chosenWords = []
    randNums = random.sample(range(len(wordList)), NUM_CARDS)
   
    index = 0
    for i in CardType:
        num = i.value
        while num > 0:
            chosenWords.append(Card(wordList[randNums[index]].lower(),i.name))
            num -= 1
            index += 1
            print(i.name)
    random.shuffle(chosenWords)
    return chosenWords

#displays the 25 randomly selected words
def displayBoard(chosenWords):

    index = 0
    for i in range(SIZE):
        for j in range(SIZE):
            chosenWords[index].printWord()
            index  +=  1
        print("\n") 

#Card class
class Card:
    #initializes
    def __init__(self, word, typeOfCard):
        self.word = word
        self.typeOfCard = typeOfCard
        print("setting card type to:",self.typeOfCard)

    #prints the word
    def printWord(self):
        print('{0: ^16}'.format(self.word), end="")

def printKey(key):
    index = 0
    for i in range(SIZE):
        for j in range(SIZE):
            print('{0: ^15}'.format(key[index].typeOfCard), end = "")
            index += 1
        print()

def main():
    wordList = loadWords()
    chosenWords = selectWords(wordList)
    displayBoard(chosenWords)
    printKey(chosenWords)
    #key = createKey()
    #printKey(key)
    #print(CardType.CardTYPE[0])
    #for i in CardType:
    #    print(i.value)
main()
