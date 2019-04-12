from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import PIL.ImageOps
print(tf.__version__)

img1 = Image.open("./boots.jpg")
img2 = Image.open("./dress.jpg")
img3 = Image.open("./shirt.jpg")
img1 = img1.convert('L')
img2 = img2.convert('L')
img3 = img3.convert('L')
img1 = PIL.ImageOps.invert(img1)
img2 = PIL.ImageOps.invert(img2)
img3 = PIL.ImageOps.invert(img3)
img1 = img1.resize([28,28])
img2 = img2.resize([28,28])
img3 = img3.resize([28,28])
img1.save("workedImg1.jpg")
img2.save("workedImg2.jpg")
img3.save("workedImg3.jpg")

img1 = np.array(img1)/255
img2 = np.array(img2)/255
img3 = np.array(img3)/255
picArray = [img1,img2,img3]
picArray = np.array(picArray)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)

train_images = train_images / 255.0


plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)


test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(test_images)

predictions2 = model.predict(picArray)

test_loss, test_acc = model.evaluate(picArray, [9,3,6])

print(np.argmax(predictions2[0]))
print(class_names[np.argmax(predictions2[0])])
print(np.argmax(predictions2[1]))
print(class_names[np.argmax(predictions2[1])])

print(np.argmax(predictions2[2]))
print(class_names[np.argmax(predictions2[2])])


def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1]) 
  predicted_label = np.argmax(predictions_array)
 
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

