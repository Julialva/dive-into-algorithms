from keras.models import load_model
from keras_preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
import matplotlib.pyplot as plt
import numpy as np
res = {
    0: 'cat',
    1: 'dog'
}
catdog = load_model("ML/cats_and_dogs_small_pretrained.h5")
imgs = {
    "gatito": "9.jpg",
    "akita 1": "akita.jpeg",
    "romi 1": "romi.jpeg",
    "romi 2": "romi2.jpeg",
    "romi 3": "romi3.jpeg",
    "akita 2": "akita2.jpeg",
    "akita 3": "akita3.jpeg"
}
for key, v in imgs.items():
    img = image.load_img(f"ML/doggies/{v}", target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x/255
    pred = (catdog.predict(x) > 0.5).astype("int32")[0, 0]
    print(f"{key} is a: {res[pred]}")
