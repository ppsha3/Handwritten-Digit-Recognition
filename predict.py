from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from numpy import  argmax

def predict():
    model = load_model('recognition_model.h5')

    predict_image = load_img('image.jpg', target_size = (28, 28), color_mode='grayscale')
    predict_image = img_to_array(predict_image)
    predict_image = predict_image.reshape(1, -1)

    # predict the result
    result = model.predict(predict_image)

    return argmax(result)

print(predict())