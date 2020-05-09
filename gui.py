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
        App.red = IntVar()
        App.blue = IntVar()
        self.display_image()
        self.wordList = codeNames.loadWords()
        self.chosenWords = codeNames.selectWords(self.wordList)
        self.createButtons()
        self.setTimer()
        self.setTeamCards()

    # reveals the type of card (flips the card)
    def wordClicked(self, index):
        self.texts[index].set(self.chosenWords[index].typeOfCard)
        self.chosenWords[index].guessed = TRUE
        self.updateTeamCards()

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
        tk.Button(center, text="STOP TIMER" , font = ("",18), command=lambda y=index: self.wordClicked(y)).pack(ipadx=10, padx=5, pady=10, side=tk.BOTTOM)
        center.pack(side = BOTTOM)
    
    # updates the number of cards left for each team
    def updateTeamCards(self):
        red = codeNames.remainingCards(self.chosenWords, "RED")
        blue = codeNames.remainingCards(self.chosenWords, "BLUE")
        self.red.set(red)
        self.blue.set(blue)

        # pops up a message that a team has lost
        if red == 0:
            self.popupmsg("The RED team LOST")
            self.resetGame()
        elif blue == 0:
            self.popupmsg("The BLUE team LOST")
            self.resetGame()

    # Places the number of cards for each team
    def setTeamCards(self):
        bottom = Frame(self)
        part = Frame(bottom)
        red = Frame(part)

        #count = IntVar()
        self.red.set(codeNames.remainingCards(self.chosenWords, "RED"))
        tk.Label(red, text = "RED TEAM cards left: ", font = ("",18)).pack(side=LEFT)
        tk.Label(red, textvariable = self.red, font = ("",18)).pack(side=RIGHT)

        blue = Frame(part)
        #count2 = IntVar()
        self.blue.set(codeNames.remainingCards(self.chosenWords, "BLUE"))
        tk.Label(blue, text = "BLUE TEAM cards left: ", font = ("",18)).pack(side=LEFT)
        tk.Label(blue, textvariable = self.blue, font = ("",18)).pack(side=RIGHT)

        red.pack(side = TOP)
        blue.pack(side=BOTTOM)
        part.pack(side = BOTTOM)
        bottom.pack(side = BOTTOM)

    # starts the timer and counts down to zero
    def startTimer(self):
        self.x.set(self.x.get() - 1)   
        if self.x.get() > 0:
            self.after(1000, self.startTimer)
        else:
            self.restartTimer()
            self.popupmsg("You have RUN out of TIME!")

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
        image = Image.open("secret_agent.jpg")
        image = image.resize((270, 180), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(image = photo)
        self.label.image = photo
        self.label.pack(side = TOP)
    
    # creates the pop up message that the user ran out of time 
    def popupmsg(self, msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup, text = msg)
        label.pack(side="top", fill="x", pady=5, padx=10)
        B1 = tk.Button(popup, text ="Ok", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    # resets the game after the game is over
    def resetGame(self):
        self.wordList = codeNames.loadWords()
        self.chosenWords = codeNames.selectWords(self.wordList)
        self.createButtons()
        self.setTimer()
        self.setTeamCards() 

root = tk.Tk()
app = App(master=root)
app.master.title("Code Names")
app.master.maxsize(50000,50000)
app.mainloop()