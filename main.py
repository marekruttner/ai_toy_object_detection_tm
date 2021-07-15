import time


from PIL import Image, ImageOps
import numpy as np
#from camera import get_frame
import camera
from ai_magic import Ai
#from lcd_driver import Display

ai = Ai('converted_tflite')

for i in range(0,100):
    #image = Image.open('IMG_2060.jpg')
    image = camera.get_frame()
    print('frame get')
    ai.classify_image(image)
    print(ai.get_prediction())
    #lcd.clear()
    #lcd.write(ai.get_prediction())
    #time.sleep(5)




