import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

from ai_magic import Ai

image = Image.open('C:\\Users\\David\\Pictures\\Pochod-Alpy\\IMG_2060.jpg')

ai = Ai('converted_savedmodel')
ai.lables
ai.predict_img(image)

print(ai.get_prediction())




