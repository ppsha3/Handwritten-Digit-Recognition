from keras.models import load_model
from numpy import  argmax
import matplotlib.pyplot as plt
import cv2
import numpy as np


def image_processing():
    predict_image = cv2.imread('image.jpg')           # loading image and converting to gray scale
    predict_image = cv2.cvtColor(predict_image, cv2.COLOR_RGB2GRAY)
    predict_image = cv2.pyrDown(predict_image)    # downsizing the image and retaining the useful info
    predict_image = cv2.pyrDown(predict_image)
    predict_image = cv2.pyrDown(predict_image)
    predict_image = cv2.pyrDown(predict_image)

    dummy = np.zeros((3, 29), dtype=np.int32)               # adding rows and deleting a column so as the array becomes 28*28
    predict_image = np.append(predict_image, dummy, axis=0)
    predict_image= np.delete(predict_image, 1, axis=1)

    plt.imshow(predict_image)
    plt.xticks([])
    plt.yticks([])
    plt.show()

    predict_image = predict_image / 255
    predict_image = predict_image.reshape(1, -1)          # flattening the array

    return predict_image


def predict():
    model = load_model('recognition_model.h5')
    predict_image = image_processing()
    result = model.predict(predict_image)               # predict the result

    return argmax(result)

# print(predict())