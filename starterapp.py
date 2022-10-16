from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color

import os
import runpy
import webbrowser

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


bgc = Color(0, 1, 0)
black = [0, 0, 0, 0]

class AiToySoftware(App):
    def aBtn1Action(self, instance):
        os.system("python "+DIR_PATH+'/main.py')

    def aBtn2Action(self):
        os.system("python "+DIR_PATH+'/dataset_capture/main.py')

    def bBtn1Action(self, instance):
        os.system("python "+DIR_PATH+'/model_copy.py')
        
    def bBtn2Action(self, instance):
        webbrowser.open('https://www.nvias.org/', new=1)

    def build(self):
        mainBox = BoxLayout(orientation="vertical")

        abboveBox = BoxLayout(orientation="horizontal")

        white = [1, 1, 1, 1]
        black = [0, 0, 0, 0]

        bgc = Color(0, 1, 0)

        aBtn1 = Button(text="TM image recognition",
                        background_color=(255, 255, 255),
                        color=(150, 0, 100, 1),
                        font_size=32,
                        size_hint=(0.7, 1))
        aBtn1.bind(on_press=self.aBtn1Action)
        aBtn2 = Button(text="Dataset taker",
                        background_color=(255, 255, 255),
                        color=(150, 0, 100, 1),
                        font_size=32,
                        size_hint=(0.7, 1))

        abboveBox.add_widget(aBtn1)
        abboveBox.add_widget(aBtn2)

        belowBox = BoxLayout(orientation="horizontal")

        bBtn1 = Button(text="Model copier",
                        background_color=(255, 255, 255),
                        color=(150, 0, 100, 1),
                        font_size=32,
                        size_hint=(0.7, 1))
        bBtn2 = Button(text="Nvias.org",
                        background_color=(255, 255, 255),
                        color=(150, 0, 100, 1),
                        font_size=32,
                        size_hint=(0.7, 1))
        bBtn2.bind(on_press=self.bBtn2Action)

        belowBox.add_widget(bBtn1)
        belowBox.add_widget(bBtn2)

        mainBox.add_widget(abboveBox)
        mainBox.add_widget(belowBox)

        return mainBox

main = AiToySoftware()
main.run()

