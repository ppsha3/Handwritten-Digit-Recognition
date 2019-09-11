# Pre-processing the data

import numpy as np
from keras.utils import to_categorical
from keras.datasets import mnist
from keras import Sequential
from keras import layers
import matplotlib.pyplot as plt
import pandas as pd

# we import the data set from the pre-loaded keras datasets package
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# there are 60000 samples of '28 x 28' array
# we will resize this '28 x 28' into 784(28*28) row vector.
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

# change the type of the array so that we can regularize the numbers
X_train = X_train.astype('int')
X_test = X_test.astype('int')

# we will divide the array to reduce the value of the data,
# so that we can perform the operation easily
X_train = X_train/255
X_test = X_test/255

# change to the categorical values for multi-class classification
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
model.add(layers.Dense(28, activation='relu', input_shape=(784,)))
model.add(layers.Dense(28, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, batch_size = 100, epochs=15)

test_loss, test_acc = model.evaluate(X_test, y_test)

print('Test Acc:', test_acc)

model.save('recog_model.h5', overwrite=True)
