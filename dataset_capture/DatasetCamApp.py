import datetime

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
import datetime
import os
from camera4kivy import Preview
os.environ["KIVY_VIDEO"] = "ffpyplayer"
from time import  sleep
from vizualize import video_inp

import cv2

class MainWidget(Widget):
    def btn_show_popup(self):
        show_popup(self)

    def btn_take(self):
        take(self)

    """
    def image_show(self):
        show_video(self)
    """
    """
    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        cv2.waitKey(1)
        return layout
    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        cv2.imshow("CV2 Image", frame)
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1
    """

    """
    def build(self):
        #layout = MDBoxLayout(orientation='vertical')
        # self.image = Image(size=("600dp", "350dp"), pos=("50dp", "200dp"))
        self.image = Image()
        #layout.add_widget(self.image)
        # layout.add_widget(self.image, size_hint=("600dp", "350dp"), pos_hint={"50dp", "200dp"})
        # layout.add_widget(self.image,pos_hint={"50dp", "200dp"})
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0 / 30)
        return Image
    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tostring()
        #for RPI change colorfmt='bgr' to colorfmt='rgba'
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture
    """


class P(FloatLayout):
    global value
    value = 1

    def on_close_popup(self):
        create_folder(self)
        window.dismiss()
    
    def create_folder_btn(self):
        global new_button
        global value
        global user_input

        user_input = self.ids.textinput.text 

        if value == 1:
            new_button = Button(text=user_input)
            self.main_widget.add_widget(new_button) 
            new_button.pos = "350dp", "90dp"
            new_button.background_color = 255, 255, 255, 1
            new_button.color = 0, 0, 0, 1
            value = 2
            
            

        elif value == 2:
            
            if new_button.text != user_input:
                new_button1 = Button(text=user_input)
                self.main_widget.add_widget(new_button1) 
                new_button1.pos = "250dp", "90dp"
                new_button1.background_color = 255, 255, 255, 1
                new_button1.color = 0, 0, 0, 1
                value = 3

            else:
                new_button1 = Button(text=user_input + str(value))
                self.main_widget.add_widget(new_button1) 
                new_button1.pos = "250dp", "90dp"
                new_button1.background_color = 255, 255, 255, 1
                new_button1.color = 0, 0, 0, 1
                value = 3 

        elif value == 3:
            if new_button.text or new_button1.text == user_input:
                new_button2 = Button(text=user_input + str(value))
                self.main_widget.add_widget(new_button2) 
                new_button2.pos = "150dp", "90dp"
                new_button2.background_color = 255, 255, 255, 1
                new_button2.color = 0, 0, 0, 1
                value = 4
            else: 
                new_button2 = Button(text=user_input)
                self.main_widget.add_widget(new_button2) 
                new_button2.pos = "150dp", "90dp"
                new_button2.background_color = 255, 255, 255, 1
                new_button2.color = 0, 0, 0, 1
                value = 4
            

        elif value == 4:
            if  new_button.text or new_button1.text or new_button2.text == user_input:
                new_button3 = Button(text=user_input + str(value))
                self.main_widget.add_widget(new_button3) 
                new_button3.pos = "50dp", "90dp"
                new_button3.background_color = 255, 255, 255, 1
                new_button3.color = 0, 0, 0, 1
                value = 5
            else:
                new_button3 = Button(text=user_input)
                self.main_widget.add_widget(new_button3) 
                new_button3.pos = "50dp", "90dp"
                new_button3.background_color = 255, 255, 255, 1
                new_button3.color = 0, 0, 0, 1
                value = 5
                
        elif value == 5:
            window.dismiss()

class KivyCamera(Image):

    source = ObjectProperty(0)

    #fps = NumericProperty(300)
    """
    def __init__(self, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self._capture = None
        if self.source is not None:
            self._capture = cv2.VideoCapture(self.source)
        #Clock.schedule_interval(self.update, 1.0 / 30)
        while True:
            self.update()
    """
    """
    def on_source(self, *args):
        if self._capture is not None:
            self._capture.release()
        self._capture = cv2.VideoCapture(self.source)
    """
    #@property

    #def capture(self):
        #return self._capture

    def __init__(self, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = cv2.VideoCapture(self.source)
        #while True:
        Clock.schedule_interval(self.update, 1.0/30.0)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt="bgr"
            )
            image_texture.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
            self.texture = image_texture
            #return image_texture

class DatasetCamApp(App):
    pass



def show_popup(main_widget):
    global window
    global user_input
    show = P()
    show.main_widget = main_widget  
    window = Popup(title="", content=show, size_hint=(None, None),size=("250dp","250dp"))
    window.open()

def take(main_widget):
        cap = cv2.VideoCapture(0)
        count = 0
        while cap.isOpened():
            _, frame = cap.read()
            #if _:
            d = datetime.datetime.now()
            cv2.imwrite(f"./dataset/{user_input}/{user_input}_{d}.png", frame)
            sleep(1)
            cv2.waitKey(0)
            break
        cap.release()


def create_folder(self):
    folder_name = user_input
    try:
        os.makedirs("./dataset/"+folder_name)
    except:
        os.makedirs("./dataset/"+folder_name + str(value - 1))

main = DatasetCamApp()
main.run()
