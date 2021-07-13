import time

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from camera import get_frame
from ai_magic import Ai
from lcd_driver import Display

ai = Ai('converted_savedmodel')
lcd =  Display()
for i in range(0,100):
    image = get_frame()
    ai.predict_img(image)
    lcd.clear()
    lcd.write(ai.get_prediction())
    time.sleep(5)




