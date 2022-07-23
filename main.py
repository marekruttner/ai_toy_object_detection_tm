#!/usr/bin/env python3

#import camera
from ai_magic import Ai
#from lcd_driver import Display
import time
#import RPi.GPIO as GPIO
#import signal
import sys


ai = Ai('converted_tflite')
"""lcd = Display()
BUTTON_GPIO = 26
run = False"""

"""def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)"""

"""
def button_pressed_callback(channel):
    print('Click')
    lcd.clear()
    image = camera.get_frame()
    ai.classify_image(image)
    print(ai.get_prediction())
    lcd.write(str(ai.get_prediction()[0]))
    lcd.new_line()
    lcd.write(str(ai.get_prediction()[1]))
"""
def main():
    while True:
        image = camera.get_image_stream()
        ai.classify_image(image)
        print(ai.get_prediction())

if __name__ == '__main__':
    lcd.write('     NVIAS     ')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING,
                          callback=button_pressed_callback, bouncetime=500)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    while(True):
        time.sleep(1)



