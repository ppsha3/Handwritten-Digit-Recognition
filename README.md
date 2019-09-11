# Handwritten-Digit-Recognition
A simple neural network to recognise handwritten/hand drawn numbers using TensorFlow, Keras in Python

How to use?

1) Run the main.py file and it will display a blank black screen. You can draw in this black screen and after you are done click on guess.
2) The model will guess the display the number in the white surface below the clear button

The neural network - 

1) The data(train/test) for this network is obtained from pre-loaded keras.datasets library. All you have to do is import keras.datasets and call the load method. The dataset comes from the MNIST datasets and keras automatically splits your data into test and train(how awesome is that?!)
2) Before we do something with the data, let's get familiar with it. The dataset contains 60000 examples of images, each being a 28*28 matrix, representing the value of pixels. There are also 10000 images loaded as the test set on which, as the name suggests, we will test our model accuracy. Note - these images have just one layer(greyscale).
3) In pre-processing, we re-organize that 28*28 array into a 784 dimensional column vector so that it is convenient for the model to perform operations.
4) In second step, we will divide the values of the pixels in that matrix with 255(max value for a colour). This will level the value of the pixels which makes it easier for the network to process it
5) The third and last step is to setup the 'Y' variable, which contains the correct 'answers' to those examples, as a 10 dimensional column vector. 10 dimensional because we are classifying the digits from 0 to 9, so, each row in the column vector corresponds to one of the 10 digits.
6) Now, the neural network. We simply create a sequential model which means the output of one layer is the input of the next layer(as in a sequence). We have 2 layers(a hidden layer and an output layer) and one 784 vector input layer. The hidden layer consists of 28 neurons with 'relu' as the activation function. The model is optimized using 'Adam' with 'categorical_crossentropy' being the loss function(which often goes with classification problems)
7) You can experiment with these algorithms




Note - This model shall soon be updated with the latest version
