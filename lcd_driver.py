import pylcdlib
import time
import sys

class Display:
    def __init__(self, addres = 0x27):
        self.lcd = pylcdlib.lcd(addres,1)
        self.lcd.lcd_write(0x01)
        self.lcd.lcd_puts(str('Nvias'), 1)


    def write(self,text):
        self.lcd.lcd_puts(str(text), 1)
        self.lcd.lcd_backlight(1)
    def clear(self):
        self.lcd.lcd_clear()