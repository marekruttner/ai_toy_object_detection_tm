from RPLCD import i2c
import time
import sys

class Display:
    def __init__(self, addres = 0x27):
        #TODO opravit nastavování
        lcdmode = 'i2c'
        cols = 16
        rows = 2
        charmap = 'A00'
        i2c_expander = 'PCF8574'
        address = 0x27
        port = 1

        self.lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                          cols=cols, rows=rows)


    def write(self,text):
        self.lcd.write_string(text)


    def clear(self):
        self.lcd.clear()
        time.sleep(0.1)

    def new_line(self):
        self.lcd.crlf()