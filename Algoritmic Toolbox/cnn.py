import streamlit as st
import tensorflow as tf
from keras.preprocessing import image
from PIL import Image
import numpy as np
import time

indecies = ["Cancer", "No-Cancer"]
model = tf.keras.models.load_model('oral_cancer_densenet_model.h5')
def diagonisis(x):
    if x == "Cancer":
        with st.spinner("Getting diagonisis..."):
            time.sleep(3)
        st.write("Some random diagonisis")
    else:
        with st.spinner("Getting diagonisis..."):
            time.sleep(3)
        st.write("Some random diagonisis")

def predict():
    result = list(model.predict(img)[0])
    value =  (max(result))
    x = ""
    if value >= 0.75:
        st.success("Cancer")
        x += "Cancer"
    else:
        st.success("No-Cancer")
        x += "No"

    diagonisis(x)

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
    st.image(raw, width=300)
    if st.button("Predict"):
        predict()