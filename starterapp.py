from kivy.app import App
from kivy.uix.widget import Widget
import os
import runpy
import webbrowser

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class MainWidget(Widget):
    def ICbtnAction(self):
        os.system("python "+DIR_PATH+'/main.py')
        
    def DCbtnAction(self):
        os.system("python "+DIR_PATH+'/dataset_capture/main.py')

    def MCbtnAction(self):
        os.system("python "+DIR_PATH+'/model_copy.py')
        
    def NVbtnAction(self):
        webbrowser.open('https://www.nvias.org/', new=1)

    def ODbtnAction(self):
        pass

    def FMbtnAction(self):
        pass
    def SbtnAction(self):
        exit()



class StarterApp(App):
    pass


main = StarterApp()
main.run()