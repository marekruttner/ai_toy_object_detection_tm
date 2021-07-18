import time

#!/usr/bin/env python3
from PIL import Image, ImageOps
import numpy as np
#from camera import get_frame
import camera
from ai_magic import Ai
from lcd_driver import Display
import time
import RPi.GPIO as GPIO
import signal
import sys


ai = Ai('converted_tflite')
lcd = Display()
BUTTON_GPIO = 26
run = True

for i in range(0,100):
    #image = Image.open('IMG_2060.jpg')
    image = camera.get_frame()
    print('frame get')
    ai.classify_image(image)
    print(ai.get_prediction())
    lcd.clear()
    lcd.write(str(ai.get_prediction()[0]))
    time.sleep(5)



BUTTON_GPIO = 26


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_pressed_callback(channel):
    global run
    if(run):
         run = False
    else:
         run = True



if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING,
                          callback=button_pressed_callback, bouncetime=100)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    while(run):
        # image = Image.open('IMG_2060.jpg')
        image = camera.get_frame()
        print('frame get')
        ai.classify_image(image)
        print(ai.get_prediction())
        lcd.clear()
        lcd.write(str(ai.get_prediction()[0]))
        time.sleep(5)


