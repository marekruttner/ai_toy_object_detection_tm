from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import os


class MainWidget(Widget):
    def btn_show_popup(self):
        show_popup(self)  


class P(FloatLayout):
    global value
    value = 1


    def on_close_popup(self):
        create_folder(self)
        window.dismiss()
    
    def create_folder_btn(self):
        global new_button
        global value


        if value == 1:
            new_button = Button(text=self.ids.textinput.text)
            self.main_widget.add_widget(new_button) 
            new_button.pos = "350dp", "90dp"
            new_button.background_color = 255, 255, 255, 1
            new_button.color = 0, 0, 0, 1
            value = 2
            
            

        elif value == 2:
            
            if new_button.text != self.ids.textinput.text:
                new_button1 = Button(text=self.ids.textinput.text)
                self.main_widget.add_widget(new_button1) 
                new_button1.pos = "250dp", "90dp"
                new_button1.background_color = 255, 255, 255, 1
                new_button1.color = 0, 0, 0, 1
                value = 3

            else:
                new_button1 = Button(text=self.ids.textinput.text + str(value))
                self.main_widget.add_widget(new_button1) 
                new_button1.pos = "250dp", "90dp"
                new_button1.background_color = 255, 255, 255, 1
                new_button1.color = 0, 0, 0, 1
                value = 3 

        elif value == 3:
            if new_button.text or new_button1.text == self.ids.textinput.text:
                new_button2 = Button(text=self.ids.textinput.text + str(value))
                self.main_widget.add_widget(new_button2) 
                new_button2.pos = "150dp", "90dp"
                new_button2.background_color = 255, 255, 255, 1
                new_button2.color = 0, 0, 0, 1
                value = 4
            else: 
                new_button2 = Button(text=self.ids.textinput.text)
                self.main_widget.add_widget(new_button2) 
                new_button2.pos = "150dp", "90dp"
                new_button2.background_color = 255, 255, 255, 1
                new_button2.color = 0, 0, 0, 1
                value = 4
            

        elif value == 4:
            if  new_button.text or new_button1.text or new_button2.text == self.ids.textinput.text:
                new_button3 = Button(text=self.ids.textinput.text + str(value))
                self.main_widget.add_widget(new_button3) 
                new_button3.pos = "50dp", "90dp"
                new_button3.background_color = 255, 255, 255, 1
                new_button3.color = 0, 0, 0, 1
                value = 5
            else:
                new_button3 = Button(text=self.ids.textinput.text)
                self.main_widget.add_widget(new_button3) 
                new_button3.pos = "50dp", "90dp"
                new_button3.background_color = 255, 255, 255, 1
                new_button3.color = 0, 0, 0, 1
                value = 5
                
        elif value == 5:
            window.dismiss()

class DatasetCamApp(App):
    pass

def show_popup(main_widget):
    global window
    show = P()
    show.main_widget = main_widget  
    window = Popup(title="", content=show, size_hint=(None, None),size=("250dp","250dp"))
    window.open()


def create_folder(self):
    folder_name = self.ids.textinput.text
    try:
        os.makedirs(folder_name)
    except:
        os.makedirs(folder_name + str(value - 1))

    
main = DatasetCamApp()
main.run()