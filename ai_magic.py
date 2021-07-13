import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np


class Ai:
    def __init__(self,model_path):
        self.model_path = model_path
        self.model = tensorflow.keras.models.load_model(model_path+'/model.savedmodel')
        self.__load_labels()


    def predict_img(self,image):
        np.set_printoptions(suppress=True)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = self.model.predict(data)
        self.last_prediction = prediction
        return prediction

    def get_labels(self):
        return self.lables

    def get_prediction(self):
        maximum = np.max(self.last_prediction)
        index_of_maximum = np.where(self.last_prediction == maximum)
        return self.lables[index_of_maximum[1][0]] , maximum

    def __load_labels(self):
        with open(self.model_path+'/labels.txt', 'r') as f:
            labels = f.readlines()
            labels = list(map(lambda s: s.strip(), labels))
            self.lables = labels
