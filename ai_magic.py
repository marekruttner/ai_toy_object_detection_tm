from PIL import Image
import tensorflow as tf

from PIL import Image, ImageOps
import numpy as np


class Ai:
    def __init__(self,model_path):
        self.model_path = model_path
        self.__load_labels()
        self.interpreter = tf.lite.Interpreter(model_path+'/model_unquant.tflite')
        self.interpreter.allocate_tensors()
        _, self.height, self.width, _ = self.interpreter.get_input_details()[0]['shape']

    def get_labels(self):
        return self.lables

    def get_prediction(self):
        maximum = np.max(self.last_prediction)
        index_of_maximum = np.where(self.last_prediction == maximum)
        return self.lables[index_of_maximum[0][0]] , maximum

    def __load_labels(self):
        with open(self.model_path+'/labels.txt', 'r') as f:
            labels = f.readlines()
            labels = list(map(lambda s: s.strip(), labels))
            self.lables = labels

    def set_input_tensor(self, image):
        tensor_index = self.interpreter.get_input_details()[0]['index']
        input_tensor = self.interpreter.tensor(tensor_index)()[0]
        input_tensor[:, :] = image

    def classify_image(self, image, top_k=1):
        image = ImageOps.fit(image, (self.height,self.width), Image.ANTIALIAS)
        """Returns a sorted array of classification results."""
        self.set_input_tensor(image)
        self.interpreter.invoke()
        output_details = self.interpreter.get_output_details()[0]
        output = np.squeeze(self.interpreter.get_tensor(output_details['index']))
        positions = self.interpreter.get_tensor(output_details['index'])
        #classes = np.squeeze(self.interpreter.get_tensor(output_details['index']))
        #scores = np.squeeze(self.interpreter.get_tensor(output_details['index']))
        
        #print(positions) #DEV STUFF comment all line in final version 
        #print(classes) #DEV STUFF comment all line in final version
        #print(scores) #DEV STUFF comment all line in final version

        #boxes = self.interpreter.get_tensor(output_details['index'])[0]
        """
        clases = self.interpreter.get_tensor(output_details['classes_idx']['index'])[0]
        scores = self.interpreter.get_tensor(output_details['scores_idx'])[0]
        """

        # If the model is quantized (uint8 data), then dequantize the results
        if output_details['dtype'] == np.uint8:
            scale, zero_point = output_details['quantization']
            output = scale * (output - zero_point)

        ordered = np.argpartition(-output, top_k)
        self.last_prediction = output
        self.positions = positions
    """
    def bbox(self):
        
        #boxes_idx, classes_idx, scores_idx = 1, 3, 0

        self.interpreter.invoke()
        output_details = self.interpreter.get_output_details()[0]

        boxes = self.interpreter.get_tensor(output_details['index'])[0]
        
        clases = self.interpreter.get_tensor(output_details['classes_idx']['index'])[0]
        scores = self.interpreter.get_tensor(output_details['scores_idx'])[0]
        
        return boxes
    """
