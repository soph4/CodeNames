import tkinter as tk
from PIL import ImageTk, Image

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.display_image()
    
    def create_widgets(self):
        self.hello = tk.Button(self)
        self.hello["text"] = "Welcome to Code Names\n(click me)"
        self.hello["command"] = self.welcome()
        self.hello.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT",fg="red",command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    def welcome(self):
        print("Hello welcome to the game!")
    
    def display_image(self):
        image = Image.open("cute-dog.jpg")
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

