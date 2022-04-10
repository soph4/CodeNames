from distutils.util import change_root
from webbrowser import BackgroundBrowser
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import mainthread
import codeNames
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.core import window
from kivy.config import Config 
from kivy.uix.relativelayout import RelativeLayout 

Config.set('graphics', 'resizable', True)

COLS = 5
ROWS = 5

class codeNamesGame(Widget):
    pass

class RedLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            #Color(1, 0, 0, 1.0)
            Color(219/255.0, 0/255.0, 0/255.0, 1.0)
            Rectangle(pos=self.pos, size=self.size)

class BlueLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            #Color(0, 0, 1, 1.0)
            Color(13/255.0, 91/255.0, 225/255.0, 1.0)
            Rectangle(pos=self.pos, size=self.size)

class BottomLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 1, 1, 1.0)
            Rectangle(pos=self.pos, size=self.size)

class codeNamesApp(App):
    
    main_layout = BoxLayout(orientation='vertical')
    top_layout = BoxLayout(orientation='horizontal')
    bottom_layout = BoxLayout(orientation='horizontal',
                              size_hint=(1, .1))

    scrollView = ScrollView()
    gridLayout = GridLayout(size_hint=(1,1))

    gridLayout.cols = 5
    gridLayout.bind(minimum_height=gridLayout.setter('height'))

    main_layout.add_widget(top_layout)
    main_layout.add_widget(gridLayout)
    main_layout.add_widget(bottom_layout)
    
    def changeColorRed(self, instance):
        #instance.background_normal = ''
        #instance.background_color = (1.0, 0.0, 0.0, 1.0)
        self.red_cards = self.red_cards - 1
        instance.background_down = "Red_card.jpg"
        instance.background_normal = "Red_card.jpg"
        #instance.background_down = ''
        self.btnCreate.text = 'Red team cards left: ' + str(self.red_cards)
        #instance.background_color = (241/255.0, 179/255.0, 179/255.0, 1.0)
        if self.red_cards == 0:
            self.bottom_label.text = 'Red team WON!!!'
            for elements in self.gridLayout.children:
                elements.disabled = True
            self.startButton.disabled = False
            self.startButton.text = 'Play again?'
        elif self.turn == 'BLUE':
            self.bottom_label.text = 'Red team\'s turn!'
            self.turn = 'RED'

    def changeColorBlue(self, instance):
        #instance.background_normal = ''
        #instance.background_color = (0.0, 0.0, 1.0, 1.0)
        self.blue_cards = self.blue_cards - 1
        instance.background_down = "Blue_card.jpg"
        instance.background_normal = "Blue_card.jpg"
        #instance.background_down = ''
        self.btnDelete.text = 'Blue team cards left: ' + str(self.blue_cards)
        if self.blue_cards == 0:
            self.bottom_label.text = 'Blue team WON!!!'
            for elements in self.gridLayout.children:
                elements.disabled = True
            self.startButton.disabled = False
            self.startButton.text = 'Play again?'
        elif self.turn == 'RED':
            self.bottom_label.text = 'Blue team\'s turn!'
            self.turn = 'BLUE'

    def changeColorBlack(self, instance):
        instance.background_normal = "Assassin_card.jpg"
        instance.text = ''
        instance.background_down = ''
        if self.turn == 'RED':
            self.bottom_label.text = 'Blue team WON!!!'
        else:
            self.bottom_label.text = 'Red team WON!!!'
        for elements in self.gridLayout.children:
            elements.disabled = True
        self.startButton.disabled = False
        self.startButton.text = 'Play again?'

    def changeColorYellow(self, instance):
        instance.background_normal = "Bystander_card.jpg"
        instance.background_down = ''
        if self.turn == 'RED':
            self.turn = 'BLUE'
            self.bottom_label.text = 'Blue team\'s turn!'
        else: #self.turn == 'BLUE
            self.turn = 'RED'
            self.bottom_label.text = 'Red team\'s turn!'

    def intermediateCard(self, instance):
        instance.background_down = 'Press_down.jpg'

    def btn_create(self, instance):
        self.gridLayout.clear_widgets()
        self.red_cards = 8
        self.blue_cards = 9
        self.bottom_label.text = 'Red team\'s turn!'
        self.btnCreate.text = 'Cards left for the RED team: ' + str(self.red_cards)
        self.btnDelete.text = 'Cards left for the BLUE team: ' + str(self.blue_cards)
        self.turn = 'RED'

        wordList = codeNames.loadWords()
        words = codeNames.selectWords(wordList)
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                button = Button(text=str(words[count].word)+ words[count].typeOfCard, 
                                font_size=50,
                                background_normal = 'orig_cards.jpg',
                                color=(0,0,0,1),
                                )
                button.bind(on_press=self.intermediateCard)
                if words[count].typeOfCard == 'RED':
                    button.bind(on_release=self.changeColorRed)
                elif words[count].typeOfCard == 'BLUE':
                    button.bind(on_press=self.changeColorBlue)
                elif words[count].typeOfCard == 'ASSASSIN':
                    button.bind(on_press=self.changeColorBlack)
                else:
                    button.bind(on_press=self.changeColorYellow)
                self.gridLayout.add_widget(button)
                count +=1 
        instance.disabled = True

    def build(self):
        self.top_layout.size_hint=(1, .1)
        self.red_cards = 8
        self.blue_cards = 9
        self.turn = 'RED'

        sm = ScreenManager()
        screen_names = ['Player view', 'Spymaster view']
        for i in range(2):
            screen = Screen(name=screen_names[i])
            sm.add_widget(screen)

        self.btnCreate = RedLabel(text='Cards left for the RED team: ' + str(self.red_cards),
                                    font_size = 80,
                                    size_hint=(2, 1))

        self.startButton = Button(font_size=80)
        self.startButton.text = 'Start'
        self.startButton.bind(on_press=self.btn_create)

        self.btnDelete = BlueLabel(text='Cards left for the BLUE team: ' +  str(self.blue_cards),
                                font_size = 80,
                                size_hint=(2, 1))

        self.top_layout.add_widget(self.btnCreate)
        self.top_layout.add_widget(self.startButton)
        self.top_layout.add_widget(self.btnDelete)

        self.bottom_label = BottomLabel(text='Red team\'s turn!', 
                                font_size=80, 
                                size_hint=(1,1),
                                color=(0,0,0,1))
        self.bottom_layout.add_widget(self.bottom_label)

        return self.main_layout

if __name__ == '__main__':
    codeNamesApp().run()