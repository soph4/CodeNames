# File: codeNames.py
# Description:


NUM_CARDS = 25

import random

# loads the words from a given text file
def loadWords():

	fileName = input("Please enter word list: ")
	text = open(fileName, "r")

	words = []

	for line in text:
		line = line.strip()
		words.append(line)

	return words

# prints the give list
def printList(wordList):

	for i in range(len(wordList)):
		print(wordList[i])	
	

# randomly selects 25 words for the game
def selectWords(wordList):
	
	chosenWords = []
	randNums = random.sample(range(len(wordList)), NUM_CARDS)
	for i in range(len(randNums)):
		chosenWords.append(wordList[randNums[i]])

	return chosenWords

def main():
	wordList = loadWords()
	#printList(wordList)
	printList(selectWords(wordList))

main()
