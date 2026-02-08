import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import models
from keras.preprocessing import image

model = models.load_model("Dog_Cat_Classify.keras")

img_path = "PATH_OF_IMAGE"

img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)

if prediction[0][0] > 0.5:
  print("Predicted: Dog")
else:
  print("Predicted: Cat")