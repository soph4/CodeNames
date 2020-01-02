from tkinter import *
import tkinter as tk
import codeNames
from PIL import ImageTk, Image

class App(tk.Frame):
    # contains all the possible words
    wordList = []
    # 25 randomly selected words for the game 
    chosenWords = []
    texts=[]

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        App.x = IntVar()
        self.wordList = codeNames.loadWords()
        self.chosenWords = codeNames.selectWords(self.wordList)
        self.createButtons()
        self.setTimer()
        self.setTeamCards()

    def wordClicked(self, index):
        print(index)
        self.texts[index].set(self.chosenWords[index].typeOfCard)

    # creates 5 by 5 grid of board of words
    def createButtons(self):
        index= 0
        center = Frame(self)
        for i in range(5):
            row = Frame(center)
            for j in range(5):
                self.texts.append(StringVar())
                self.texts[index].set(self.chosenWords[index].word)
                tk.Button(row, textvariable = self.texts[index] , font = ("",18), command=lambda y=index: self.wordClicked(y)).pack(ipadx=10, padx=5, pady=10, side=tk.BOTTOM)
                index += 1
            row.pack(ipadx=5, side = LEFT)

        center.pack(side = BOTTOM)

    def setTeamCards(self):
        bottom = Frame(self)
        part = Frame(bottom)
        tk.Label(part, text = "RED TEAM cards left: ", font = ("",18)).pack(side=LEFT)
        tk.Label(part, text = "BLUE TEAM cards left: ", font = ("",18)).pack(side=RIGHT)
        part.pack(side = BOTTOM)
        bottom.pack(side = BOTTOM)


    # starts the timer and counts down to zero
    def startTimer(self):
        self.x.set(self.x.get() - 1)   
        if self.x.get() > 0:
            self.after(1000, self.startTimer)
        else:
            self.restartTimer()

    # resets the timer back to one minute 
    def restartTimer(self):
        self.x.set(60)

    # creates and sets the timer for the game
    def setTimer(self):
        top = Frame(self)
        time = Frame(top)
        tk.Button(time, text = "PRESS TO START", font = ("",18), command = self.startTimer).pack(side = LEFT)
        tk.Label(time, text = "TIMER:", font = ("",18)).pack(side = LEFT)
        self.x.set(60)
        tk.Label(time, textvariable = self.x, font = ("", 18)).pack(side = RIGHT)
        time.pack(side = LEFT)
        top.pack(side = TOP)

    # extra function to display images 
    def display_image(self):
        image = Image.open("cute_dog.jpg")
        image = image.resize((190,250), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(image = photo)
        self.label.image = photo
        self.label.pack()
    
root = tk.Tk()
app = App(master=root)
app.master.title("Code Names")
app.master.maxsize(1500,50000)
app.mainloop()

