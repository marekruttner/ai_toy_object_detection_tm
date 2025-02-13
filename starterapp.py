from kivy.app import App
from kivy.uix.widget import Widget
import os
import runpy
import webbrowser

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class MainWidget(Widget):
    def ICbtnAction(self):
        os.system("python3 " + DIR_PATH + '/main.py')

    def DCbtnAction(self):
        os.system("python3 " + DIR_PATH + '/dataset_capture/main.py')

    def MCbtnAction(self):
        os.system("python3 " + DIR_PATH + '/model_copy.py')

    def NVbtnAction(self):
        webbrowser.open('https://www.nvias.org/', new=1)

    def ODbtnAction(self):
        os.system("python3 " + DIR_PATH + '/effeciend_net/detect.py')

    def FMbtnAction(self):
        os.system('nemo')

    def XTbtnAction(self):
        os.system("xterm")

    def SbtnAction(self):
        os.system('sudo shutdown')


class StarterApp(App):
    pass


main = StarterApp()
main.run()