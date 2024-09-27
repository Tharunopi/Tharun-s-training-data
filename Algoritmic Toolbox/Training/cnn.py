import streamlit as st
import tensorflow as tf
from keras.preprocessing import image
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('oral_cancer_densenet_model.h5')

raw = st.file_uploader(
    "Choose a image",
    accept_multiple_files=False,
    type=["png", "jpeg"]
    )

if raw is not None:
    img = Image.open(raw)
    img = img.resize((224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    st.image(raw)

def predict():
    result = model.predict(img)[0]
    st.success(result)