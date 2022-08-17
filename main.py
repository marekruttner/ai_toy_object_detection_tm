#!/usr/bin/env python3

from camera import *
from ai_magic import Ai
#from lcd_driver import Display
import time
#import RPi.GPIO as GPIO
#import signal
import sys
import cv2
import numpy as np


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

def visualize(image):
    """
    for i in range(len(prediction)):
        image = np.array(image)

        color = (0, 0, 255)
        boxes = ai.bbox()
        imW, imH = int(width), int(height)
        #boxes = boxes

        ymin = int(max(1, (boxes[i][0] * imH)))
        xmin = int(max(1, (boxes[i][1] * imW)))
        ymax = int(min(imH, (boxes[i][2] * imH)))
        xmax = int(min(imW, (boxes[i][3] * imW)))

        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
    """
    prediction = ai.classify_image(image)
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    position = np.squeeze(ai.positions)
    for i in range(len(ai.positions)):
        color = (0, 0, 255)
        imW, imH = int(width), int(height)
        
        print(ai.get_prediction())
        print(position)
        """
        ymin = int(1 * (position[0] * imH))
        xmin = int(1 * (position[1] * imW))
        ymax = int(ymin * (position[0] * imH))
        xmax = int(xmin * (position[1] * imW))
        """
        ymin = int(position[1] * imH)
        xmin = int(position[0] * imW)
        ymax = int(position[1] * imH + ymin)
        xmax = int(position[0]* imW + xmin)
        
        print(xmin, ymin, xmax, ymax)

        #cv2.rectangle(image, (xmax, ymax), (xmin, ymin), color, 2)
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
        cv2.imshow("image",image) 
    #cv2.imshow("image",image)
    


def main():
    while True:
        image = get_image_stream()
        #prediction = ai.classify_image(image)
        #print(ai.get_prediction()) #DEV STUFF comment all line in final version
        #print(ai.positions) #DEV STUFF comment all line in final version
        visualize(image)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        

    print("SUCCESSFULY DONE ;-)")

if __name__ == '__main__':
    """
    lcd.write('     NVIAS     ')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING,
                          callback=button_pressed_callback, bouncetime=500)

    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    while(True):
        time.sleep(1)
    """
    main()



