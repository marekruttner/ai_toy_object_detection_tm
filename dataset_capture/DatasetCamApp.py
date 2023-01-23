from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import os


class MainWidget(Widget):
    def btn_show_popup(self):
        show_popup()
 

    
class P(FloatLayout):
    
    def on_close_popup(self):
        print(self.ids.input.text)
        create_folder(self)
        window.dismiss()
        
class DatasetCamApp(App):
    pass

def show_popup():
    global window
    show = P()
    window = Popup(title="", content=show, size_hint=(None, None),size=("250dp","250dp"))
    window.open()

def create_folder(self):
    folder_name = self.ids.input.text
    os.makedirs(folder_name)
    
        

main = DatasetCamApp()
main.run()