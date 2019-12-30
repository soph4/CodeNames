from tkinter import *
import tkinter as tk
import random
import codeNames
from PIL import ImageTk, Image

wordList = codeNames.loadWords()
#creates a list of 25 Cards
chosenWords = codeNames.selectWords(wordList)

root = tk.Tk()
root.title("Code Names")

#sets up the timer at the top of the program
topPart = Frame(root)
timer = tk.Label(topPart, text = "TIMER").pack(side = LEFT)
topPart.pack(side=TOP)

#creates the 5*5 grid of words 
centerPart = Frame(root)
index = 0
for i in range(5):
    row = Frame(centerPart)
    for j in range(5):
        word = chosenWords[index].word
        tk.Button(row, text = word ,command=lambda: update_text(1)).pack(padx=5, pady=10, side=tk.BOTTOM)
        index += 1
    row.pack(side = LEFT)
centerPart.pack(side = TOP)

# sets up the card counter for both teams 
redLabel = tk.Label(root, text = "RED team cards left")
redLabel.pack(side = BOTTOM)
blueLabel = tk.Label(root, text = "BLUE team cards left")
blueLabel.pack(side = BOTTOM)
    


root.mainloop()