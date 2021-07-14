import time

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
#from camera import get_frame
from ai_magic import Ai
#from lcd_driver import Display

ai = Ai('converted_savedmodel')

for i in range(0,100):
    #image = get_frame()
    #print('frame get')
    ai.predict_img([1,1])
    print(ai.get_prediction())
    lcd.clear()
    lcd.write(ai.get_prediction())
    time.sleep(5)




