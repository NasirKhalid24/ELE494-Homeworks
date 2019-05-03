# -*- coding: utf-8 -*-
"""Homework3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G7_9EbtyyIUtZUFfh3KWWBVt5vSY1U94
"""

# All required imports

import pickle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import keras

(training_images, training_labels), (testing_images, testing_labels) = keras.datasets.cifar10.load_data()

label_names = ["Airplane", "Automobile", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"]

print("Shape of training images: " + str(training_images.shape))
print("Shape of training labels: " + str(training_labels.shape))
print("Shape of testing images: " + str(testing_images.shape))
print("Shape of testing labels: " + str(testing_labels.shape))
print("\n")
r = np.random.randint(50001)
plt.imshow(training_images[r])
plt.title('Image {}: Label #{} (Image of {})'.format(r, training_labels[r], label_names[training_labels[r][0]]))

# Function to plot loss and accuracy vs epochs
def loss_curve(history):
  train_loss = history.history['loss']
  val_loss = history.history['val_loss']
  x_axis     = range(1, len(history.history['loss'])+1)
  
  plt.figure()
  plt.plot(x_axis, train_loss, label="Training Loss")
  plt.plot(x_axis, val_loss, label="Validation Loss")
  plt.ylabel('Loss Value')
  plt.xlabel('Epochs')
  plt.title('Epochs vs Loss')
  plt.legend()
  
def acc_curve(history):
  train_acc  = history.history['acc']
  val_acc = history.history['val_acc']
  x_axis     = range(1, len(history.history['acc'])+1)
  
  plt.figure()
  plt.plot(x_axis, train_acc, label="Training Accuracy")
  plt.plot(x_axis, val_acc, label="Validation Accuracy")
  plt.ylabel('Accuracy Value')
  plt.xlabel('Epochs')
  plt.title('Epochs vs Accuracy')
  plt.legend()

# Start creating neural network
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.utils import to_categorical

Nasir_Net = Sequential() #Custom Model

# One hot encoding for training output
output_training = to_categorical(training_labels, len(label_names))

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
              
# Compiling Network
Nasir_Net.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with Batch Normalization
from keras.layers.normalization import BatchNormalization

Nasir_Net = Sequential() #Custom Model with Batch Normalization

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
              
# Compiling Network
Nasir_Net.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

plt.figure()
plt.imshow(training_images[1])
plt.title("Original Image")

print("Original Pixel Value: " + str(training_images[0][0][0][0]))

training_images = training_images.astype('float32')
testing_images = testing_images.astype('float32')

training_images_mean = training_images.mean(axis=(1,2), keepdims=True)
testing_images_mean = testing_images.mean(axis=(1,2), keepdims=True)

training_images -= training_images_mean
testing_images -= testing_images_mean

print("Mean Subtracted Pixel Value: " + str(training_images[0][0][0][0]))

plt.figure()
plt.imshow(training_images[1])
plt.title("Mean Subtracted Image")

training_images_std = training_images.std(axis=(1,2), keepdims=True)
testing_images_std = testing_images.std(axis=(1,2), keepdims=True)

training_images /= training_images_std
testing_images /= testing_images_std

print("Mean Subtracted and STD Normalized Pixel Value: " + str(training_images[0][0][0][0]))

plt.figure()
plt.imshow(training_images[1])
plt.title("Mean Subtracted and STD Normalized Image")

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with random_uniform initialization
from keras.layers.normalization import BatchNormalization

Nasir_Net = Sequential() #Custom Model with random_uniform initialization

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3), kernel_initializer='random_uniform', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3), kernel_initializer='random_uniform', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Conv2D(64,(3,3), padding='same', kernel_initializer='random_uniform', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3), kernel_initializer='random_uniform', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512, kernel_initializer='random_uniform', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512, kernel_initializer='random_uniform', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
              
# Compiling Network
Nasir_Net.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with random_uniform initialization
from keras.layers.normalization import BatchNormalization

Nasir_Net = Sequential() #Custom Model with random_uniform initialization

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3), kernel_initializer='glorot_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3), kernel_initializer='glorot_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Conv2D(64,(3,3), padding='same', kernel_initializer='glorot_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3), kernel_initializer='glorot_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512, kernel_initializer='glorot_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512, kernel_initializer='glorot_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
              
# Compiling Network
Nasir_Net.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with ones initialization
from keras.layers.normalization import BatchNormalization

Nasir_Net = Sequential() #Custom Model with ones

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3), kernel_initializer='ones', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3), kernel_initializer='ones', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Conv2D(64,(3,3), padding='same', kernel_initializer='ones', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3), kernel_initializer='ones', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512, kernel_initializer='ones', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512, kernel_initializer='ones', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
              
# Compiling Network
Nasir_Net.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with lecun_normal initialization
from keras.layers.normalization import BatchNormalization

Nasir_Net = Sequential() #Custom Model with lecun_normal

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3), kernel_initializer='lecun_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3), kernel_initializer='lecun_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Conv2D(64,(3,3), padding='same', kernel_initializer='lecun_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3), kernel_initializer='lecun_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512, kernel_initializer='lecun_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512, kernel_initializer='lecun_normal', bias_initializer='zero'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
              
# Compiling Network
Nasir_Net.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with Dropout

Nasir_Net = Sequential() #Custom Model with Dropout

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
              
# Compiling Network
Nasir_Net.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with different learning rate
from keras import optimizers

Nasir_Net = Sequential() #Custom Model with Dropout

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
         
custom_rmsprop = keras.optimizers.RMSprop(lr=0.002, rho=0.9, epsilon=None, decay=0.0)
# Compiling Network
Nasir_Net.compile(optimizer=custom_rmsprop,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with SGD
from keras import optimizers

Nasir_Net = Sequential() #Custom Model with SGD

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
         

# Compiling Network
Nasir_Net.compile(optimizer='SGD',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with Adam
from keras import optimizers

Nasir_Net = Sequential() #Custom Model with Adam

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
         

# Compiling Network
Nasir_Net.compile(optimizer='Adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with Nadam
from keras import optimizers

Nasir_Net = Sequential() #Custom Model with Nadam

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
         

# Compiling Network
Nasir_Net.compile(optimizer='Nadam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with Nadam changed parameters
from keras import optimizers

Nasir_Net = Sequential() #Custom Model with Nadam changed parameters

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
         
p = keras.optimizers.Nadam(lr=0.008, beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.01)

# Compiling Network
Nasir_Net.compile(optimizer=p,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=32,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

# Rebuilding Network with Nadam
from keras import optimizers

Nasir_Net = Sequential() #Custom Model with Nadam

# Architecture of Network
Nasir_Net.add(Conv2D(32,(3,3),padding='same',input_shape=(32, 32, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))
    
Nasir_Net.add(Conv2D(32,(3,3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Conv2D(64,(3,3), padding='same'))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Conv2D(64,(3, 3)))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(MaxPooling2D(pool_size=(2,2)))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Flatten())
Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dense(512))
Nasir_Net.add(BatchNormalization())
Nasir_Net.add(Activation('relu'))

Nasir_Net.add(Dropout(0.5))

Nasir_Net.add(Dense(len(label_names)))
Nasir_Net.add(Activation('softmax'))
         

# Compiling Network
Nasir_Net.compile(optimizer='Nadam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
Nasir_Net.summary()

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=128,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")

x = Nasir_Net.fit(training_images,
                  output_training,
                  batch_size=512,
                  epochs=15,
                  validation_split=0.1,
                  verbose=1)

loss_curve(x)
acc_curve(x)

output_testing = to_categorical(testing_labels, len(label_names))

score = Nasir_Net.evaluate(testing_images, output_testing, batch_size=32)
print("Accuracy on test data: " + str(score[1] * 100) + "%")