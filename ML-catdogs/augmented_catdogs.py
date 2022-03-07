from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import os
import matplotlib.pyplot as plt
from random import randint
REF = '/home/jk'
train_cats_dir = f'{REF}/Downloads/cats_and_dogs_small/train/cats'

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')
fnames = [os.path.join(train_cats_dir, fname) for
          fname in os.listdir(train_cats_dir)]
img_path = fnames[randint(0, len(fnames))]
img = image.load_img(img_path, target_size=(150, 150))
plt.figure(0)
imgplot = plt.imshow(img)
x = image.img_to_array(img)
x = x.reshape((1,) + x.shape)
i = 1
for batch in datagen.flow(x, batch_size=1):
    plt.figure(i)
    imgplot = plt.imshow(image.array_to_img(batch[0]))
    i += 1
    if i % 5 == 0:
        break
plt.show()
