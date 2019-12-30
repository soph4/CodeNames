from tkinter import *
import tkinter as tk
import random
import codeNames
from PIL import ImageTk, Image

NUM_CARDS = 25

class App(tk.Frame):
    wordList = []
    chosenWords = []

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.wordList = codeNames.loadWords()
        #self.loadWords()
        self.selectWords()
        self.createButtons()
        #self.create_widgets()
        #self.display_image()
    
    def update_text(string):
        print("String: ", string)

    def loadWords(self):
        #fileName = input("Please enter word list: ")
        #if(fileName == ""):
        fileName = "wordlist2.txt"
        text = open(fileName, "r")
        
        words = []
        for line in text:
            line = line.strip()
            words.append(line)
        self.wordList = words

    def selectWords(self):
        chosen = []
        randNums = random.sample(range(len(self.wordList)), NUM_CARDS)
   
        index = 0
        while index < NUM_CARDS:
            chosen.append(self.wordList[randNums[index]].lower())
            index += 1
        random.shuffle(chosen)
        self.chosenWords = chosen

    def createButtons(self):
        index = 0
        for i in range(5):
            row = Frame(self)
            for j in range(5):
                word = self.chosenWords[index]
                tk.Button(row, text = word ,command=lambda: update_text(1)).pack(padx=5, pady=10, side=tk.BOTTOM)
                index += 1
            row.pack(side = LEFT)


    def create_widgets(self):
        #string = "bye"
        self.hello = tk.Button(self, text="hello", command=lambda: update_text(1)).pack()
        #self.hello["text"] = "Welcome to Code Names\n(click me)"
        #self.hello["command"] = self.welcome()
        #self.hello.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT",fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    def welcome(self):
        print("Hello welcome to the game!")
    
    #def update_text(string):
    #    print("String:", string)

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
app.master.maxsize(1000,4000)
app.mainloop()

